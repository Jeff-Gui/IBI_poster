# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:26:33 2019

@author: 王梓洋
"""

DNA="ATGCTTCAGAAAGGTCTTACG"
myDict={}
for word in DNA:
    if word in myDict:
        myDict[word]+=1
    else:
        myDict[word]=1
myDict

GCcontent = (myDict['C']+myDict['G'])/(myDict['C']+myDict['T']+myDict['A']+myDict['G'])
print("GC content is " + str(GCcontent))