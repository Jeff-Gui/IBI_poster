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

------SAMPLE HERE-------

Please input your sequence:
ATGCTTCAGAAAGGTCTTACG

Please input a threshold:
0.0001
  position     segment     prot_name  possibility
0     5-11     TTCAGAA          SPIB     0.000180
1     6-12     TCAGAAA          SPIB     0.000946
2    15-20      TCTTAC  MAFG::NFE2L1     0.000233
3     9-17   GAAAGGTCT         SNAI2     0.000133
4     9-18  GAAAGGTCTT         NR4A1     0.002600
        
@author: IBI group1
"""

import os
os.chdir('/Users/jefft/Desktop/ZJE/IBI(local)/git_repository/IBI_poster/Jeff') #change working directory

import numpy as np
import re
import pandas as pd
nmlist = []
segment=[]
position=[]
possibility=[]
data = open('JASPARdbs.txt').readlines()
dic = {'A':0, 'C':1, 'G':2, 'T':3}
seq = input('Please input your sequence:\n')
trd = float(input('Please input a threshold:\n'))

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
        for j in range(0, len(seglist)):
            for k in range(0, col):
                psb = psb * a[dic[seglist[j][k]], k]
               
            if psb > trd:          # determine whether possibility is over the threshold
                name=re.findall(r'\t(.+?)\n',data[5*t])[0]
                possibility.append(psb)
                nmlist.append(name)
                segment.append(seglist[j])
                p=str(j+1)+'-'+str(j+col)
                position.append(p)
            psb = 1 #reset
df=pd.DataFrame({'position':position, 'segment':segment,'prot_name':nmlist,'possibility':possibility})                
print(df)
        
