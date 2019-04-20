#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 22:30:57 2019

@Jeff 
    This script is for testing the user interface.
    Now, the input of task 5 supports mRNA and protein sequence,
    maybe we can have DNA imput in the future.

@author: ibi group1
"""
import re
seq = ''
opt = ''
opt2 = ''
s = 0
#-----------------------------MAIN FUNCTION------------------------------------
def ui():
    global seq
    global opt
    global opt2
    global s
    print('Select your task:\n[1]:GC content calculation [2]:complementary sequence [3]:mRNA [4]:peptide [5]:hydropathy [0]:exit', end='')
    opt = input('')
    ckopt()
    if opt == 0:
        s = 1
        return
    elif opt == 4:
        print('Input your mRNA sequence:',end='')
        seq = input('')
        ckmrna()
    elif opt == 5:
        print('Select your sequence type:\n[1]: protein sequence [2]mRNA sequence',end='')
        opt2 = input('')
        ckopt2()
        print('Input your sequence:',end='')
        seq = input('')
        ckmrna()
    elif opt in {1,2,3}:
        print('Input your DNA sequence',end='')
        seq = input('')
        ckdna()
    return 
#------------------------------------------------------------------------------
def ckopt():
    """
    check the number input when selecting task
    """
    global opt
    if re.search('[^123450]',opt):
        print('Please input the correct number:',end='')
        opt = input('')
        if not ckopt():
            return False
    else:
        opt = int(opt)
    return True
 
def ckopt2():
    """
    check the number input when selecting sequence type in task 5
    """
    global opt2
    if re.search('[^12]',opt2):
        print('Please input the correct number:',end='')
        opt2 = input('')
        if not ckopt2():
            return False
    else:
        opt2 = int(opt2)
    return True
       
def ckdna():
    """
    check DNA
    maybe add into task 5 in the future?
    """
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
    """
    check mRNA
    assumptions:
        1. if sequence length is not 3n, then it only contains one AUG (initial condon) and one stop condon
        2. if sequence length is 3n, then it is 'part' of a whole peptide
    """
    global seq
    p = re.findall('AUG[AUCG]*(UAA)|AUG[AUCG]*(UAG)|AUG[AUCG]*(UGA)', seq) #only consider one initial condon and one stop condon
    try:
        seq = p[0]
        return True
    except:         #if sequence length is times of 3
        if len(seq)%3==0 and not re.search('[^AUCG]',seq): #assume that sequence is meaningful(can be translated)
            return True
        else:
            print('Please input the correct mRNA sequence:', end='')
            seq = input('')
            if not ckmrna():
                return False
    return True

def ckpt():
    """
    check protein
    """
    global seq
    if re.search('[^GAVLIMFWPSTCYNQDEKRH]',seq):
        print('Please input the correct protein sequence:', end='')
        seq = input('')
        if not ckpt():
            return False
    else:
        return True
    return True

#---------------------------EXECUTE--------------------------------------------
while s==0:
    ui()