#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:58:01 2019
-------COMMENTS HERE--------
- Jeff
    现在可以完成的功能：
        输入指定单链DNA, 检索所有579个蛋白对应长度的dna片段与蛋白结合的概率
        概率阈值设定在0.01，超过则输出matrix号码，名称，对应dna片段
        输出在answer list里
    可能的改进:
        输出dna片段的位置 或 可视化
- Robin

- Harper
        
@author: IBI group1
"""

import os
os.chdir('/Users/jefft/Desktop/ZJE/IBI(local)/git_repository/IBI_poster/Jeff') #change working directory

import numpy as np
import re
nmlist = []
data = open('JASPARdbs.txt').readlines()

dic = {'A':0, 'C':1, 'G':2, 'T':3}
seq = input('Please input your sequence:\n')
trd = float(input('Please input a threshold:\n'))
answer = []
for t in range(0, 579): #database has 2895 lines with 579 matrices
    nm = re.findall('\d+', data[5*t+1])    
    col = int(len(nm)) #col is the length of dna segment
    a = np.zeros((4,col))
    seglist = []
    for s in range(0,len(seq)-col+1):
        seglist.append(seq[s:s+col])
    #every possible segment of input dna is stored in seglist
    if seglist:
        for i in range(5*t+1,5*t+5): # i : the number of matrix lines
            nm = re.findall('\d+', data[i])
            for j in range(0,col):
                a[i-5*t-1,j] = int(nm[j])
        add = a[0,0]+a[1,0]+a[2,0]+a[3,0] #count the number of sample DNA sequence
        a = (1/add)*a
        psb = 1 #possibility that segment can bind with protein
        for seg in seglist:
            for k in range(0, len(seg)):
                psb = psb * a[dic[seg[k]], k]
            if psb > trd:          # determine whether possibility is over the threshold
                answer += [data[5*t] + ' ' + seg]
            psb = 1 #reset
                
                
        
