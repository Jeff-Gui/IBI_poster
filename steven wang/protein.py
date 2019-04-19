# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:47:32 2019

@author: 王梓洋
"""

DNA="ATGCTTCAGAAAGGTCTTACG"
print(DNA.find("TCA"))
DNAtemplate = DNA[(DNA.find("TCA")):(DNA.find("TTA")+3)]
def save(filename, contents):
 fh = open(filename, 'w', encoding='utf-8')
 fh.write(contents)
 fh.close()
save('/Users/王梓洋/.spyder-py3/dnatemplate.txt', DNAtemplate)
with open('/Users/王梓洋/.spyder-py3/dnatemplate.txt', "w", encoding='utf-8') as f:
 f.write(DNAtemplate)
fh = open('/Users/王梓洋/.spyder-py3/dnatemplate.txt', 'w', encoding='utf-8')
fh.write(DNAtemplate)
fh.close()

def mRNA(seq):
    ntComplement = {'A':'U', 'C':'G', 'T':'A', 'G':'C'}
     
    revSeqList = list(seq)
    revComSeqList = [ntComplement[k] for k in revSeqList]
 
    revComSeq = ''.join(revComSeqList)
    return revComSeq
 
seq = ''
with open('/Users/王梓洋/.spyder-py3/dnatemplate.txt') as f:
    for line in f:
        line = line.rstrip()
        seq += line.upper()
         
print ("mRNA chain = " + mRNA(seq))

mRNAtemplate = mRNA(seq)
def save(filename, contents):
 fh = open(filename, 'w', encoding='utf-8')
 fh.write(contents)
 fh.close()
save('/Users/王梓洋/.spyder-py3/rnatemplate.txt', mRNAtemplate)
with open('/Users/王梓洋/.spyder-py3/rnatemplate.txt', "w", encoding='utf-8') as f:
 f.write(mRNAtemplate)
fh = open('/Users/王梓洋/.spyder-py3/rnatemplate.txt', 'w', encoding='utf-8')
fh.write(mRNAtemplate)
fh.close()

def Protein(seq):
    ntComplement = {'A':'U', 'C':'G', 'U':'A', 'G':'C'}
     
    revSeqList = list(seq)
    revComSeqList = [ntComplement[k] for k in revSeqList]
 
    revComSeq = ''.join(revComSeqList)
    return revComSeq

seq = ''
with open('/Users/王梓洋/.spyder-py3/rnatemplate.txt') as f:
    for line in f:
        line = line.rstrip()
        seq += line.upper()
         
print ("protein chain = " + Protein(seq))