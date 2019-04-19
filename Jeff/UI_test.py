#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 22:30:57 2019

@author: jefft
"""
import re
seq = ''

def a():
    return 1
def b():
    return 2
def c():
    return 3
def d():
    return 4
def e():
    return 5
dic = {1:a(), 2:b(), 3:c(), 4:d(), 5:e()}

def ui():
    global seq
    print('Select your task:\n[1]:GC content calculation [2]:complementary sequence [3]:mRNA [4]:peptide [5]:hydropathy [0]:exit', end='')
    opt = input('')
    if opt == 0:
        exit()
    elif opt == 4:
        print('Input your mRNA sequence:',end='')
        seq = input('')
    elif opt == 5:
        print('Input your mRNA or amino acid sequence:',end='')
        seq = input('')
    elif opt in {1,2,3}:
        print('Input your DNA sequence',end='')
        seq = input('')
    else:
        print('Please input the correct number:',end='')
        opt = input('')
        ui()
    return opt

def ckdna(x):
    global seq
    if re.search('[^ATCG]', x):
        print('Please input the correct DNA sequence:', end='')
        seq = input('')
        if not ckdna(seq):
            return False
    else:
        return True
    return True
    
print('Please input the correct DNA sequence:', end='')
seq = input('')
