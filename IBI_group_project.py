#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 23:07:33 2019

@author: jefft
"""
import re
import numpy as np   
pdbs = np.array([[['F','F','L','L'],['S','S','S','S'],['Y','Y','*','*'],['C','C','*','W']],
             [['L','L','L','L'],['P','P','P','P'],['H','H','Q','Q'],['R','R','R','R']],
             [['I','I','I','M'],['T','T','T','T'],['N','N','K','K'],['S','S','R','R']],
             [['V','V','V','V'],['A','A','A','A'],['D','D','E','E'],['G','G','G','G']]])
dic3 = {'U':0,'C':1,'A':2,'G':3}    
#------------------------------------------------------------------------------
        
def GC_content(x):
    count = 0
    for base in x:
        if base == 'G' or base == 'C':
            count += 1
    print('GC content of total bases:' , '{:.2%}'.format(count/len(x)))
    
#------------------------------------------------------------------------------

def cplmty(x):
    dic = {'A':'T','T':'A','C':'G','G':'C'}
    cm = ''
    for base in x:
        cm += dic[base]
    cm = cm[::-1]
    print('Complementary DNA strand (5\' to 3\'):\n', cm)

#------------------------------------------------------------------------------

def mrna(x):
    dic2 = {'A':'U','T':'A','C':'G','G':'C'}
    mrna = ''
    for base in x:
        mrna += dic2[base]
    mrna = mrna[::-1]
    print('mRNA sequence is:\n', mrna)

#------------------------------------------------------------------------------
def dtp(x):
    p = ''
    if x.find('AUG')> -1:
        for i in range(x.find('AUG'), len(x)-2, 3):
            p += pdbs[dic3[x[i]], dic3[x[i+1]], dic3[x[i+2]]]
            if p[-1] == '*':
                break
        print('Peptide translated from mRNA is:\n', p[:-1])
    else:
        print('Cannot find initiation codon!')
#------------------------------------------------------------------------------
"""
This recursion function provides a user-friendly console interface.
The user can call the task funcitons for any times and exit whenever he wants.
The function contains a error-detecting part to ensure the correct input.
"""
dic = {1:GC_content, 2:cplmty, 3:mrna}
seq = ''
s = 1 # s controls whether the input of the task 1~4 is needed, if one input the wrong number at first, then the task should not be chosen before asking for a correct input
def inpt():
    global seq
    global s
    if not seq:
        seq = input('Please input your sequence:\n')
        while 1==1:    
            try:
                if re.search('[^ATCGU]', seq) or (seq.find('T') * seq.find('U') > -1):
                    print('Please input the correct sequence:', end='') #end='' ensures no extra white line after input
                    seq = input('')
                else:
                    break
            except:
                print('Please input the correct sequence:', end='')
                seq = input('')
    if s == 1: 
        opt = input('Choose your task:\n [1]:GC content calculation [2]:complementary sequence [3]:mRNA [4]:peptide [0]:exit\n')
    while 1==1:
        try:
            opt = int(opt)
            if opt == 0:
                seq = '' #reset the string for next time use
                break
            elif opt in dic.keys():
                dic[opt](seq)
                s = 1
                inpt()
                break
            else:
                print('Please input the correct number:', end='')
                opt = input('')
        except:
            print('Please input the correct number:', end='')
            opt = input('')
            s = 0
            inpt()
            break
#----------------------
a = 'ATGGTGTGAGGTGC'
a.find('AGGTT')
