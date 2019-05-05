#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:58:01 2019
-------COMMENTS HERE--------
- Jeff

- Robin

- Harper

------SAMPLE HERE-------

Please input your sequence:
ATGCTTCAGAAAGGTCTTACG
        
@author: IBI group1
"""

#import os
#os.chdir('/Users/Wyxx/Documents/git/IBI_poster/Jeff') #change working directory
import colorama
from colorama import Fore
import numpy as np
import re
import math
import pandas as pd
nmlist = []
data = open('JASPARdbs.txt').readlines()

dic = {'A':0, 'C':1, 'G':2, 'T':3}
seq = input('Please input your sequence:\n')
trd = float(input('Please input a threshold:\n'))
position = []
segment = []
score = []
for t in range(0, 579): #database has 2895 lines with 579 matrices
    nm = re.findall('\d+', data[5*t+1])    
    col = int(len(nm)) #col is the length of dna segment
    a = np.zeros((4,col))
    seglist = []
    for s in range(0,len(seq)-col+1):
        seglist.append(seq[s:s+col])
    #every possible segment of input dna is stored in seglist
    if seglist:
        # generate PFM
        for i in range(5*t+1,5*t+5): # i : the number of matrix lines
            nm = re.findall('\d+', data[i])
            for j in range(0,col):
                a[i-5*t-1,j] = int(nm[j])
        # convert PFM to PWM
        add = a[0,0]+a[1,0]+a[2,0]+a[3,0] #count the number of sample DNA sequence
        psdc = add**0.5 #pseudocount
        for m1 in range(0,4):
            for m2 in range(0,col):
                temp = a[m1,m2]
                temp = (temp+psdc/4)/(add+psdc)
                temp = math.log(temp/0.25,2)
                a[m1,m2] = temp
        sc = 0
        sd = 0
        for j in range(0, len(seglist)):
            for k in range(0, col):
                sc += a[dic[seglist[j][k]], k]
                sd += a[:, k].max()
        #determine whether the score is over the threshold
            if sc/sd > trd:
                name=re.findall(r'\t(.+?)\n',data[5*t])[0]
                score.append(sc/sd)
                nmlist.append(name)
                segment.append(seglist[j])
                p=str(j+1)+'-'+str(j+col)
                position.append(p)
                print(Fore.BLACK+seq[:j],Fore.RED+seq[j:j+col],Fore.BLACK+seq[j+col:],Fore.BLUE+name)
            sc = 0
            sd = 0
            #reset
df=pd.DataFrame({'position':position, 'segment':segment,'prot_name':nmlist,'score':score})     
print(Fore.BLACK+'---------------------------------------------------------')           
print(df)
