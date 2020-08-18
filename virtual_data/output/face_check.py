import matplotlib
import numpy as np
from func_new import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm

N_RANGE = 60
TARGET_FACTOR = 0
TARGET_FACE = 0

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

def out_kitekan_correct(data_num):
  factor = np.loadtxt("../factor_"+str(data_num+1)+".csv",delimiter=",")
  kibun = np.loadtxt("../mental_"+str(data_num+1)+".csv",delimiter=",")
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

for test_num in range(1,N_RANGE):
  phi_signal = np.zeros((EMO_NUM,N_RANGE))
  #phi_signal = np.zeros((EMO_NUM,test_num+1))
  weight = np.zeros((EMO_NUM,SIT_NUM))
  corr_out = np.zeros((SIT_NUM,EMO_NUM))
  phi_out = out_kitekan_correct(N_RANGE-1)
  #phi_out = out_kitekan_correct(test_num+1)
  signal = np.loadtxt("../face_"+str(N_RANGE)+".csv",delimiter=",")
  #signal = np.loadtxt("../face_"+str(test_num+1)+".csv",delimiter=",")
  factor = np.loadtxt("../factor_"+str(N_RANGE)+".csv",delimiter=",")
  if test_num == 0:
    signal = np.array([signal])
    factor = np.array([factor])

  weight[0,:]= np.loadtxt("./hap_weight_"+str(test_num+1)+".csv")
  weight[1,:]= np.loadtxt("./sup_weight_"+str(test_num+1)+".csv")
  weight[2,:]= np.loadtxt("./ang_weight_"+str(test_num+1)+".csv")
  weight[3,:]= np.loadtxt("./sad_weight_"+str(test_num+1)+".csv")

  #for t in range(test_num+1):
  for t in range(N_RANGE):
    for emo_num in range(EMO_NUM):
      #array = signal - phi_out[:,sit_num,:]
      for sit_num in range(SIT_NUM):

        phi_signal[emo_num,t] += weight[emo_num,sit_num]*phi_out[t,sit_num,emo_num]

  plt.scatter(factor[:,TARGET_FACTOR],phi_signal[TARGET_FACE],label="phi out"+str(test_num),color=cm.hsv(test_num/float(N_RANGE+20.0)),linewidth=0.5,linestyle='dashed')
  #plt.plot(phi_signal[0]-signal[:,0],label="phi out",color=cm.hsv(test_num/60.0))
  #x = np.linspace(0,45,45)
  #if test_num%3==0:
  #  plt.bar(x+test_num*0.1,phi_signal[0]-signal[:,0],label="phi out",color=cm.hsv(test_num/60.0),width=.1,alpha=0.5)

  plt.ylim(-0.1,0.3)
  plt.legend()
  """
  if test_num is not 44:
    plt.pause(.1)
    plt.clf()
  else:
    plt.show()
  """
#standard
plt.xlabel("val of facor["+str(TARGET_FACTOR)+"]")
plt.ylabel("val of face["+str(TARGET_FACE)+"]")
plt.plot(factor[:,TARGET_FACTOR],signal[:,TARGET_FACE],label="signal",linestyle='dashed')
plt.show()

  #for emo_num in range(EMO_NUM):
  #np.savetxt('/home/kazumi/prog/quiz_check2016/jrm_test/'+str(i_name+1)+'/face_diff_'+xlabel[emo_num]+'-29.csv',face_diff[:,emo_num],delimiter=",")

