#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from numpy.random import *

from robot_behavior import output_robot
from face_out import fact2face
from mental_out import *

TIME_LENGTH = 100
FACTOR_SIZE = 10

TYPE_OF_ACTION = 5
TYPE_OF_FACE = 4

class Factor_cal:
  def __init__(self,time_length):
    self.history = np.zeros(time_length)
    self.rate = np.zeros(time_length)
    self.point = 0
    self.win_count = 0
    self.win_point_count = 0
    self.lose_count = 0
    self.action_history=np.zeros((time_length,TYPE_OF_ACTION))

  def calc_rate_action(self,t):
    array = np.zeros(5)

    if t>5:
      for a_i in range(TYPE_OF_ACTION):
        array[a_i] = np.sum(self.action_history[t-5:t,a_i])/5.0
    else:
      for a_i in range(TYPE_OF_ACTION):
        array[a_i] = np.sum(self.action_history[:t,a_i])/float(t+1.0)
    return array

  def calc_rate(self,t):
    if t==0:
      self.rate[0] = self.history[0]
    else:
      self.rate[t] = np.mean(self.history[:t])

  def calc_point(self,t):
    if self.history[t] == True:
      self.point+=2
      self.win_count +=1
      if self.history[t-1] == True:
        self.win_point_count+=1
      else:
        self.win_point_count=1
        self.lose_point = 0
      if self.win_point_count == 5:
        self.point+=5
        print('get five')
        self.win_point_count = 0
    else:
      self.point+=-1
      if self.history[t-1] == False:
        self.lose_count +=1
      else:
        self.lose_point = 1
        self.win_count =0

  def get_ans(self,t,ans):
    self.history[t] = ans
    action = output_robot('ran',TYPE_OF_ACTION)
    self.action_history[t,int(action)] +=1
    self.calc_rate(t)
    self.calc_point(t)

  def ret_factor(self,t):
    factor = np.zeros(FACTOR_SIZE)
    factor[0] = t/80.0
    factor[1] = self.rate[t]
    factor[2:7] = self.calc_rate_action(t)
    factor[7] = (self.point+80)/320.0
    factor[8] = self.win_count/270.0
    factor[9] = self.lose_count/270.0
    return factor

#return correct or wrong to answer
def ans():
  val = rand()
  ans = 0
  if(val>0.5):
    ans = True
  else:
    ans = False
  return ans
  
def main():

  factor_class = Factor_cal(TIME_LENGTH)
  m_0 = 3.0

  virtual_factor = np.zeros((TIME_LENGTH,FACTOR_SIZE))
  virtual_mental = np.zeros(TIME_LENGTH+1)
  virtual_face = np.zeros((TIME_LENGTH,TYPE_OF_FACE))

  virtual_mental[0] = m_0
  weight = np.loadtxt('weight.csv',delimiter=",")

  for t in range(TIME_LENGTH):
    factor_class.get_ans(t,ans())
    m_0=ret_dummy_m(m_0,'inc')
    print('factor of quizz',factor_class.ret_factor(t))
    factor_val = factor_class.ret_factor(t)
    face_val = fact2face(factor_val,weight,m_0/10.0)

    virtual_factor[t,:] = factor_val
    virtual_mental[t+1] = m_0
    virtual_face[t,:] = face_val

  np.savetxt('./virtual_data/factor.csv',virtual_factor,fmt="%.3f",delimiter=",")
  np.savetxt('./virtual_data/mental.csv',virtual_mental,fmt="%.3f",delimiter=",")
  np.savetxt('./virtual_data/face.csv',virtual_face,fmt="%.3f",delimiter=",")

if __name__ == "__main__": 
  main()
