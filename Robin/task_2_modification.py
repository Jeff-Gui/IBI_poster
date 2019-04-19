# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:18:42 2019

@author: ROBIN
"""

DNAtemplate=input('please enter a DNA sequence:')
DNA=DNAtemplate.replace('G','c').replace('C','g').replace('A','t').replace('T','a')
DNA=DNA[::-1]
print(DNA.upper())
