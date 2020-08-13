#!/usr/bin/env python
# -*- coding: utf-8 -*-

from func_new import *

TYPE_OF_FACE = 4


def fact2face(factor, weight, mental):
  if factor.shape[0] is not 10:
    print('check the shapae of the factor')
    return None
  if weight.shape[1] is not 10:
    print('check the shapae of the weight')
    return None

  face_out = np.zeros((TYPE_OF_FACE,factor.shape[0]))
  for s_i in range(TYPE_OF_FACE):
    for f_i in range(factor.shape[0]):
        i = 4*s_i + f_i
        face_out[s_i]+= func(inv_norm(i,factor[f_i]/100.0),mental,i)
  return face_out

if __name__ == "__main__": 
  factor = np.ones((1,10))
  weight = np.ones((4,10))
  mental = 1
  print(fact2face(factor[0,:],weight,mental))
