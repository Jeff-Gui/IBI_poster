#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:15:09 2019

@author: caitlynjiang
"""

#ss=input('Please type in a 🧬 single strand:' )
#cpr=ss[::-1].replace('A','1').replace('T','2').replace('G','3').replace('C','4').replace('1','T').replace('2','A').replace('3','C').replace('4','G')
#cp=cpr[::-1]
#print('Double-stranded DNA:',ss)
#print('                    ',cp)

#wcount=0

while 1==1:
    ss=input('Please type in a 🧬 single strand:' )
    cpr=ss[::-1].replace('A','1').replace('T','2').replace('G','3').replace('C','4').replace('1','T').replace('2','A').replace('3','C').replace('4','G')
    cp=cpr[::-1]
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
        print('Double-stranded DNA:',ss)
        print('                    ',cp)
        print('Complementary DNA sequence(from 5’ to 3’):',cpr)
        break
    
    
  