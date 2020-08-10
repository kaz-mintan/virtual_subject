#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from numpy.random import *

from robot_behavior import output_robot

TIME_LENGTH = 30
FACTOR_SIZE = 10

TYPE_OF_ACTION = 5

class Factor_cal:
  def __init__(self,time_length):
    self.history = np.zeros(time_length)
    self.rate = np.zeros(time_length)
    self.point = 0
    self.win_count = 0
    self.win_point_count = 0
    self.lose_count = 0
    self.action_history=np.zeros((time_length,TYPE_OF_ACTION))

  def calc_rate_action():
    return some

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
    self.calc_rate(t)
    self.calc_point(t)

  def ret_factor(self,t):
    factor = np.zeros(FACTOR_SIZE)
    factor[0] = t/80.0
    factor[1] = self.rate[t]
    factor[7] = self.point
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
  
def dummy_m(size):
  if size>0:
    mental = np.zeros(size)
    delta_m = np.random.rand(size-1)
    m_0 = np.random.rand(1)
    mental[0] = m_0
    for i in range(1,size):
      mental[i] = mental[i-1] + delta_m[i-1]
  else:
    mental = None
  return mental

def main():
  factor_class = Factor_cal(TIME_LENGTH)
  for t in range(TIME_LENGTH):
    factor_class.get_ans(t,ans())
    print('factor of quizz',factor_class.ret_factor(t))
  

if __name__ == "__main__": 
  main()
