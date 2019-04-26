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
    DNA=x.replace('G','c').replace('C','g').replace('A','t').replace('T','a')
    DNA=DNA[::-1]
    print('Complementary DNA strand (5\' to 3\'):\n', DNA.upper(), sep='')

#------------------------------------------------------------------------------

def mrna(x):
    dic2 = {'A':'U','T':'A','C':'G','G':'C'}
    mrna = ''
    for base in x:
        mrna += dic2[base]
    mrna = mrna[::-1]
    print('mRNA sequence is:\n', mrna, sep='')

#------------------------------------------------------------------------------
def dtp(x):
    p = ''
    if x.find('AUG')> -1:
        for i in range(x.find('AUG'), len(x)-2, 3):
            p += pdbs[dic3[x[i]], dic3[x[i+1]], dic3[x[i+2]]]
            if p[-1] == '*':
                break
        print('Peptide translated from mRNA is:\n', p[:-1], sep='')
    else:
        print('Cannot find initiation codon!')
#------------------------------------------------------------------------------
"""
UI
This recursion function provides a user-friendly console interface.
The user can call the task funcitons for any times and exit whenever he wants.
The function contains a error-detecting part to ensure the correct input.
"""
seq = ''
opt = ''
opt2 = ''
s = 0
t = 0
#-----------------------------MAIN FUNCTION------------------------------------
def ui():
    global seq
    global opt
    global opt2
    global s
    global t
    print('Select your task:\n[1]:GC content calculation [2]:complementary sequence [3]:mRNA [4]:peptide [5]:hydropathy [0]:exit', end='')
    opt = input('')
    ckopt()
    if t == 0:
        print('Input your sequence:',end='')
        seq = input('')
        t = 1
    if opt == 0:
        s = 1
        return
    elif opt == 4:
        ckmrna()
        dtp(seq)
    elif opt == 5:
        print('Select your sequence type:\n[1]: protein sequence [2]mRNA sequence',end='')
        opt2 = input('')
        ckopt2()
        if opt2==1:
            ckpt()
        else:
            ckmrna()
    elif opt in {1,2,3}:
        ckdna()
        if opt==1:
            GC_content(seq)
        elif opt==2:
            cplmty(seq)
        else:
            mrna(seq)
    print('Keep your sequence? Y/N',end='')
    p = input('')
    if p == 'n':
        seq = ''
        t = 0
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
    p = re.findall('AUG[AUCG]*|AUG[AUCG]*|AUG[AUCG]*', seq) #only consider one initial condon and one stop condon
    try:
        seq = p[0]
        seq2 = seq[::-1] #find the last pattern of "stop condon", if 3* length in between, then valid
        if (len(seq)-seq2.find('GAU'))%3==0 or (len(seq)-seq2.find('AAU'))%3==0 or (len(seq)-seq2.find('AGU'))%3==0:
            return True
        else:
            print('Please input the correct mRNA sequence:', end='')
            seq = input('')
            if not ckmrna():
                return False
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