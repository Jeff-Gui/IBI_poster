#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:53:21 2019

@author: lanqi
"""

#give me a DNA string
s=input('Give me a DNA string : ')
#e.g. s = "ATGCTTCAGAAAGGTCTTACG"
#count the GC frequency of the string
s = list(s)
count=0
for word in s:
    if word == 'G' or word == 'C':
        count += 1        
GC=count/len(s)
#How to become percentage?
print('GC content for DNA is : ', GC)