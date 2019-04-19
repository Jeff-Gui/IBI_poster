# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:44:26 2019

@author: 王梓洋
"""

   
def reverse_complement(seq):
    ntComplement = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
     
    revSeqList = list(reversed(seq))
    revComSeqList = [ntComplement[k] for k in revSeqList]
 
    revComSeq = ''.join(revComSeqList)
    return revComSeq
 
seq = ''
with open('/Users/王梓洋/.spyder-py3/dna.txt') as f:
    for line in f:
        line = line.rstrip()
        seq += line.upper()
         
print ("complementary chain = " + reverse_complement(seq))