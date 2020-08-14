#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from numpy.random import *

def ret_dummy_m(present_m,mode):
  if mode=='ran':
    delta_m = np.random.rand()*2.0-1.0
  elif mode == 'inc':
    delta_m = 0.5
  return present_m + delta_m

