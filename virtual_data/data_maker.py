#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

virtual_factor = np.loadtxt('./factor.csv',delimiter=",")
virtual_face = np.loadtxt('./face.csv',delimiter=",")
virtual_mental = np.loadtxt('./mental.csv',delimiter=",")

print('select mode "seq" or "mov"')
mode = raw_input()
if mode == 'seq':
  print('input max time-length')
  length = int(raw_input())

  for i in range(length):
    factor_name = './factor_'+str(i+1) + '.csv'
    face_name = './face_'+str(i+1) + '.csv'
    mental_name = './mental_'+str(i+1) + '.csv'
    np.savetxt(factor_name,virtual_factor[:i+1],fmt="%.3f",delimiter=",")
    np.savetxt(mental_name,virtual_mental[:i+1],fmt="%.3f",delimiter=",")
    np.savetxt(face_name,virtual_face[:i+1],fmt="%.3f",delimiter=",")

elif moded == 'mov':
  print('input length of moving frame')
  frame_length = int(raw_input())
  print('input max time-length')
  time_length = int(raw_input())

  for i in range(time_length):
    factor_name = './factor_'+str(i+1) + '.csv'
    face_name = './face_'+str(i+1) + '.csv'
    mental_name = './mental_'+str(i+1) + '.csv'

    np.savetxt(factor_name,virtual_factor[i+1:i+1+frame_length],fmt="%.3f",delimiter=",")
    np.savetxt(mental_name,virtual_mental[i+1:i+1+frame_length],fmt="%.3f",delimiter=",")
    np.savetxt(face_name,virtual_face[i+1:i+1+frame_length],fmt="%.3f",delimiter=",")
  memo = 'moving frame length: ' + str(frame_length)+'\ntime length: ' + str(time_length)
  np.savetxt('./data memo.txt',memo)

