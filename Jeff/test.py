#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:49:40 2019

@author: jefft
"""

"""
import os
os.chdir('/Users/jefft/Desktop') #change working directory
"""

import numpy as np
data = open('test.txt').readlines()
col = int(((len(data[1])-6)/6))-1
a = np.zeros((4,col))
for i in range(1,5):
    for j in range(0,col):
        a[i-1,j] = int(data[i][7*j+4 : 7*j+10])
add = a[0,0]+a[1,0]+a[2,0]+a[3,0] #count the number of sample DNA sequence
a = (1/add)*a


"""

-------------------THE FOLLOWING CODES ARE NOT CORRECT-------------------------

"""
#solve the equation system
b = np.array([0,0,0,0]) #constant matrix
list = []
for k in range(0,col):
    c = np.array([[a[0,k]-1, a[0,k], a[0,k], a[0,k]],
                 [a[1,k], a[1,k]-1, a[1,k], a[1,k]],
                 [a[2,k], a[2,k], a[2,k]-1, a[2,k]],
                 [a[3,k], a[3,k], a[3,k], a[3,k]-1]])
    d = np.linalg.solve(c,b)
    list.append(d)
      
