import matplotlib
import numpy as np
from func_new import *
import matplotlib.pyplot as plt

EMO_NUM = 4
SIT_NUM = 10
USR_NUM = 9

xlabel = ["hap","sup","ang","sad"]

func_num = [[0,1,2,3],[4,5,6,7],[8,9,10,11],
  [12,13,14,15],[16,17,18,19],[20,21,22,23],
  [24,25,26,27],[28,29,30,31],[32,33,34,35],[36,37,38,39]]

username = ['inusan', 'kumasan', 'nekosan', 'test119', 'test120', 'test121', 'tomato', 'torisan', 'usagisan']

j=0
count_array=np.zeros((USR_NUM,4))
graph_label = ["0.1<r<0.2","0.2<r<0.3","0.3<r<0.4","0.4<r"]

def out_kitekan_correct(data_num, set_num):
  factor = np.loadtxt("../factor_"+str(data_num)+".csv",delimiter=",")
  kibun = np.loadtxt("../mental_"+str(data_num)+".csv",delimiter=",")
  if kibun.ndim == 0:
    length = 1
    kibun = np.array([kibun])
    factor = np.array([factor])
  else:
    length = kibun.shape[0]

  phi_out = np.zeros((length,SIT_NUM,EMO_NUM))
  for data_num in range(length):
    for emo_num in range(EMO_NUM):
      for sit_num in range(SIT_NUM):
        ret = func(inv_norm(func_num[sit_num][emo_num],factor[data_num][sit_num]),kibun[data_num]*10.0+0.001,func_num[sit_num][emo_num])
        phi_out[data_num][sit_num][emo_num] = ret

  return phi_out

set_num = 29
len_num =30

for test_num in range(100):
  phi_signal = np.zeros((EMO_NUM,test_num+1))
  weight = np.zeros((EMO_NUM,SIT_NUM))
  #phi_out = np.zeros((set_num,SIT_NUM,EMO_NUM))
  corr_out = np.zeros((SIT_NUM,EMO_NUM))
  phi_out = out_kitekan_correct(test_num,len_num)
  signal = np.loadtxt("../face_"+str(test_num)+".csv",delimiter=",")
  if test_num == 0:
    signal = np.array([signal])

  weight[0,:]= np.loadtxt("./hap_weight_test.csv")
  weight[1,:]= np.loadtxt("./sup_weight_test.csv")
  weight[2,:]= np.loadtxt("./ang_weight_test.csv")
  weight[3,:]= np.loadtxt("./sad_weight_test.csv")

  #weight[0,:]= np.loadtxt("./hap_weight_"+str(tag_number)+".csv")
  #weight[1,:]= np.loadtxt("./sup_weight_"+str(tag_number)+".csv")
  #weight[2,:]= np.loadtxt("./ang_weight_"+str(tag_number)+".csv")
  #weight[3,:]= np.loadtxt("./sad_weight_"+str(tag_number)+".csv")

  for t in range(test_num):
    for emo_num in range(EMO_NUM):
      #array = signal - phi_out[:,sit_num,:]
      for sit_num in range(SIT_NUM):

        phi_signal[emo_num,t] += weight[emo_num,sit_num]*phi_out[t,sit_num,emo_num]

  plt.plot(phi_signal[0],label="phi out")
  plt.plot(signal[:,0],label="signal")
  #plt.ylim(0,1)
  plt.legend()
  plt.show()

  #for emo_num in range(EMO_NUM):
  #np.savetxt('/home/kazumi/prog/quiz_check2016/jrm_test/'+str(i_name+1)+'/face_diff_'+xlabel[emo_num]+'-29.csv',face_diff[:,emo_num],delimiter=",")

