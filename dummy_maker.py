#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def dummy_f(size):
  f_0 = np.zeros(10)

  for i in range(10):
    #time of trial
    if i == 0:


    elif i == 1:


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


  

if __name__ == "__main__": 
  main()
