#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from numpy.random import *

def output_robot(mode,action_num):
  val = 0

  if mode=='ran':
    val = randint(0,action_num,1)

  return val

if __name__ == '__main__':
  TYPE_OF_ACTION = 4
  print(output_robot('ran',TYPE_OF_ACTION))
