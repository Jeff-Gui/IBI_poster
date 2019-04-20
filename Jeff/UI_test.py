#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 22:30:57 2019

@author: jefft
"""
import re
seq = ''
opt = ''

def ui():
    global seq
    global opt
    print('Select your task:\n[1]:GC content calculation [2]:complementary sequence [3]:mRNA [4]:peptide [5]:hydropathy [0]:exit', end='')
    opt = input('')
    ckopt()
    if opt == 0:
        return False
    elif opt == 4:
        print('Input your mRNA sequence:',end='')
        seq = input('')
        ckmrna()
    elif opt == 5:
        print('Input your mRNA or amino acid sequence:',end='')
        seq = input('')
        ckmrna()
    elif opt in {1,2,3}:
        print('Input your DNA sequence',end='')
        seq = input('')
        ckdna()
    
    return True

def ckopt():
    global opt
    if re.search('[^123450]',opt):
        print('Please input the correct number:',end='')
        opt = input('')
        if not ckopt():
            return False
    else:
        opt = int(opt)
    return True
        
def ckdna():
    global seq
    if re.search('[^ATCG]', seq):
        print('Please input the correct DNA sequence:', end='')
        seq = input('')
        if not ckdna():
            return False
    else:
        return True
    return True 

def ckmrna():
    global seq
    if re.search('[^AUCG]', seq):
        print('Please input the correct mRNA sequence:', end='')
        seq = input('')
        if not ckmrna():
            return False
    else:
        return True
    return True

def ckpt():
    global seq
    if re.search('[^GAVLIMFWPSTCYNQDEKRH]',seq):
        print('Please input the correct protein sequence:', end='')
        seq = input('')
        if not ckpt():
            return False
    else:
        return True
    return True

while ui():
    ui()