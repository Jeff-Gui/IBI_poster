# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:08:06 2019

@author: Wyxx
"""

DNA=input('please enter a DNA sequence:')
mRNA=DNA.replace('A','u').replace('T','a').replace('C','g').replace('G','c')
print(mRNA.upper())