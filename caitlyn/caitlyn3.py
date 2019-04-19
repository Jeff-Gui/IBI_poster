#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:25:32 2019

@author: caitlynjiang
"""

while 1==1:
    ss=input('Please type in a 🧬 single strand:' )
    rna=ss.replace('A','1').replace('T','2').replace('G','3').replace('C','4').replace('1','U').replace('2','A').replace('3','C').replace('4','G')
    wcount=0
    for i in ss:
        if i=='A':
            continue
        elif i=='T':
            continue
        elif i=='G':
            continue
        elif i=='C':
            continue
        else:
            wcount+=1
        
    if wcount>= 1:
        print('wrong DNA!')
    #ss=input('Please type in a 🧬 single strand:' )
    else:
        print('DNA:',ss)
        print('RNA:',rna)
        break