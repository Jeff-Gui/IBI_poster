# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:27:31 2019

@author: Wyxx
"""

DNA=input('please enter a DNA sequence:')#input a sequence of 
myDict={}
for word in DNA:
    if word in myDict:#count the number of ATCG (a specific kind of nucleotide)
        myDict[word]+=1
    else:
        myDict[word]=1 #There is only one such nucleotide
print(myDict)
all=myDict['A']+myDict['T']+myDict['C']+myDict['G']
GC=myDict['G']+myDict['C']
GCcontent=GC/all
print('%.2f'%(GCcontent*100),'%')

