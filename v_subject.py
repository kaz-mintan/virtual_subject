#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from func_new import *

func_num = [[0,1,2,3],[4,5,6,7],[8,9,10,11],
  [12,13,14,15],[16,17,18,19],[20,21,22,23],
  [24,25,26,27],[28,29,30,31],[32,33,34,35],[36,37,38,39]]

norm_val = np.array([80,1,1,1,1,1,1,320,80,80])

def weight_determiner(mode):
  if mode == "TMP":
    tmp_weight = np.array([[.1,.1,.2,.3],[.4,.1,.2,.4],[.1,.5,.1,.1],
      [.6,.2,.4,.1],[.1,.9,.4,.1],[.1,.1,.1,.1],
      [.1,.4,.2,.5],[.4,.1,.1,.1],[.4,.6,.2,.5],[.6,.1,.4,.2]])
    weight = tmp_weight
  if mode == "ONEK":
    print("input the id number of weight")
    num = input()
    weight = np.zeros((10,4))
    weight[int(num)-1,:] = 1
  return weight

def add_noize(val,noize_level):
  noize = np.random.rand(val.shape[0],val.shape[1])/noize_level/np.tile(norm_val,(val.shape[0],1))
  val = val + noize
  val[np.where(val>1)] = 1
  return val
  

def out_face(factor,kibun,tmp_weight):
  emotion = np.zeros((len(kibun),4))
  factor=add_noize(factor,1)
  for t in range(len(kibun)):
    for emo_num in range(4):
      for sit_num in range(10):
        emotion[t,emo_num] += tmp_weight[sit_num,emo_num]*func(inv_norm(func_num[sit_num][emo_num],factor[t,sit_num]),kibun[t]*10.0+0.001,func_num[sit_num][emo_num])
    emotion[t,:] = emotion[t,:]*1.0/np.sum(emotion[t,:])
  return emotion

def main():
  #just for building
  mode = "TMP"
  weight=weight_determiner(mode)

  #set assumed factors and kibun
  data_len = 5
  factor_ex = np.random.rand(data_len,10) 
  kibun_ex = np.random.rand(data_len)

  emotion = out_face(factor_ex,kibun_ex,weight)
  print("print output assumed facial expression",emotion)


if __name__ == "__main__": 
  main()
