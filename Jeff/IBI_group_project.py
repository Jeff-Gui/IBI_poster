#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 23:07:33 2019

@author: IBI group 1
"""

#==============================SET UP==========================================
"""
import os
wd = input('Input your working directory:\n')
#/Users/jefft/Desktop/ZJE/IBI(local)/git_repository/IBI_poster/Jeff
os.chdir(wd) #change working directory
"""

from colorama import Fore
import math
import re
import numpy as np   
import pandas as pd
pdbs = np.array([[['F','F','L','L'],['S','S','S','S'],['Y','Y','*','*'],['C','C','*','W']],
             [['L','L','L','L'],['P','P','P','P'],['H','H','Q','Q'],['R','R','R','R']],
             [['I','I','I','M'],['T','T','T','T'],['N','N','K','K'],['S','S','R','R']],
             [['V','V','V','V'],['A','A','A','A'],['D','D','E','E'],['G','G','G','G']]])
dic3 = {'U':0,'C':1,'A':2,'G':3}
data = open('JASPARdbs.txt').readlines()
seq = ''
opt = ''
s = 0
t = 0
#==============================================================================
"""
Main functions with corresponding task 1~5
"""
#===========================MAIN FUNCTIONS=====================================       
def GC_content(x):
    count = 0
    for base in x:
        if base == 'G' or base == 'C':
            count += 1
    print('\nGC content of total bases:' , '{:.2%}'.format(count/len(x)))  
#------------------------------------------------------------------------------
def cplmty(x):
    DNA=x.replace('G','c').replace('C','g').replace('A','t').replace('T','a')
    DNA=DNA[::-1]
    print('\nComplementary DNA strand (5\' to 3\'):\n', DNA.upper(), sep='')
#------------------------------------------------------------------------------
def mrna(x):
    dic2 = {'A':'U','T':'A','C':'G','G':'C'}
    mrna = ''
    for base in x:
        mrna += dic2[base]
    mrna = mrna[::-1]
    print('\nmRNA sequence is:\n', mrna, sep='')
#------------------------------------------------------------------------------
def dtp(x):
    p = ''
    if x.find('AUG')> -1:
        for i in range(x.find('AUG'), len(x)-2, 3):
            p += pdbs[dic3[x[i]], dic3[x[i+1]], dic3[x[i+2]]]
            if p[-1] == '*':
                break
        print('\nPeptide translated from mRNA is:\n', p[:-1], sep='')
    else:
        print('Cannot find initiation codon!')
#------------------------------------------------------------------------------
def tfs():
    global seq
    global data
    nmlist = []
    dic = {'A':0, 'C':1, 'G':2, 'T':3}
    trd = input('Input a threshold:\n')
    cktrd(trd)
    trd = float(trd)
    position = []
    segment = []
    score = []
    for t in range(0, 579): #database has 2895 lines with 579 matrices
        """
        Generate empty PFM
        Fragment query DNA sequence
        """
        nm = re.findall('\d+', data[5*t+1])    
        col = int(len(nm)) #col is the length of dna segment
        a = np.zeros((4,col))
        seglist = []
        for s in range(0,len(seq)-col+1):
            seglist.append(seq[s:s+col])
        """
        Segments with the same length as the matrix are stored in seglist
        """
        if seglist:
            """
            Generate PFM
            """
            for i in range(5*t+1,5*t+5):
                nm = re.findall('\d+', data[i])
                for j in range(0,col):
                    a[i-5*t-1,j] = int(nm[j])
            """
            Convert PFM to PWM
            """
            add = a[0,0]+a[1,0]+a[2,0]+a[3,0]
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
                    """
                    Determine whether the score is over the threshold
                    """
                if sc/sd > trd:
                    name=re.findall(r'\t(.+?)\n',data[5*t])[0]
                    score.append(sc/sd)
                    nmlist.append(name)
                    segment.append(seglist[j])
                    p=str(j+1)+'-'+str(j+col)
                    position.append(p)
                    print(Fore.BLACK+seq[:j],Fore.RED+seq[j:j+col],Fore.BLACK+seq[j+col:],Fore.BLUE+name)
                sc = 0
                sd = 0 #reset
    df=pd.DataFrame({'Segment position':position, 'Segment detected':segment,'Protein name':nmlist,'Relative score':score})                
    df = df.sort_values(by=['Relative score'], ascending=False)
    if df.empty:
        print('\nNothing found')
    else:
        print(Fore.BLACK+'============================================================')   
        print(df)
#==============================================================================
"""
UI
This recursion function provides a user-friendly console interface.
The user can call the task funcitons for any times and exit whenever he wants.
(ui function and execute function)
The function contains a error-detecting part to ensure the correct input.
(validation functions)
"""
#=============================UI FUNCTION======================================
def ui():
    global seq
    global opt
    global opt2
    global s
    global t
    opt = input('Select your task:\n[1]:GC content calculation [2]:Complementary sequence [3]:mRNA [4]:Peptide [5]:Transcription factor search [0]:Exit\n')
    ckopt()
    if opt == 0:
        s = 1
        return
    if t == 0:
        opt3 = input('Choose input mode:\n[F]:Fasta file [T]:Type in\n')
        if opt3=='F':
            flip()
        else:
            seq = input('Input your sequence:\n')
        t = 1
    if opt == 4:
        ckmrna()
        dtp(seq)
    elif opt in {1,2,3,5}:
        ckdna()
        if opt==1:
            GC_content(seq)
        elif opt==2:
            cplmty(seq)
        elif opt==3:
            mrna(seq)
        else:
            tfs()
    p = input('Keep your sequence? Y/N\n')
    if p == 'N' or p== 'n':
        seq = ''
        t = 0
    return 
#===========================VALIDATION FUNCTIONS===============================
def ckopt():
    """
    check the number input when selecting task
    """
    global opt
    if re.search('[^123450]',opt):
        opt = input('Please input the correct number:\n')
        if not ckopt():
            return False
    else:
        opt = int(opt)
    return True
 
def ckdna():
    """
    check DNA
    """
    global seq
    if re.search('[^ATCG]', seq):
        misip()
        if not ckdna():
            return False
    else:
        return True
    return True 

def ckmrna():
    """
    check mRNA
    assumptions:
        1. if sequence length is not 3n, then it only contains one AUG (initiation condon) and one stop condon
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
            misip()
            if not ckmrna():
                return False
    except:         #if sequence length is times of 3
        if len(seq)%3==0 and not re.search('[^AUCG]',seq): #assume that sequence is meaningful(can be translated)
            return True
        else:
            misip()
            if not ckmrna():
                return False
    return True

def ckpt():
    """
    check protein
    """
    global seq
    if re.search('[^GAVLIMFWPSTCYNQDEKRH]',seq):
        misip()
        if not ckpt():
            return False
    else:
        return True
    return True

def cktrd(x):
    """
    check the number input for threshold in task5
    """
    try:
        x = float(x)
        if not 0<x<=1:
            x = input('Please input the threshold between 0~1\n')
            if not cktrd(x):
                return False
    except:
        x = input('Please input the threshold between 0~1\n')
        if not cktrd(x):
            return False
    return True

def flip():
    global seq
    flnm = input('Input your file name:\n')
    a1 = open(flnm)
    a2 = a1.read()
    a1.close()
    for char in a2[a2.find('\n')+2:]:
        if char in {'A','T','C','G'}:
            seq += char

def misip():
    global seq
    print('\nPlease input the correct sequence.',end='')
    opt4 = input('Choose input mode:\n[F]:Fasta file [T]:Type in\n')
    if opt4=='F':
        flip()
    else:
        seq = input('Input your sequence:\n')
#=============================EXECUTE FUNCTION=================================
while s==0:
    ui()
