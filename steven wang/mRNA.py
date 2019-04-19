# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:10:15 2019

@author: 王梓洋
"""

def mRNA(seq):
    ntComplement = {'A':'U', 'C':'G', 'T':'A', 'G':'C'}
     
    revSeqList = list(seq)
    revComSeqList = [ntComplement[k] for k in revSeqList]
 
    revComSeq = ''.join(revComSeqList)
    return revComSeq
 
seq = ''
with open('/Users/王梓洋/.spyder-py3/dna.txt') as f:
    for line in f:
        line = line.rstrip()
        seq += line.upper()
         
print ("mRNA chain = " + mRNA(seq))