# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:50:20 2019

@author: Wyxx
"""

DNAtemplate=input('please enter a DNA sequence:')
DNA=DNAtemplate.replace('G','c').replace('C','g').replace('A','t').replace('T','a')
DNA=DNA[::-1]
print(DNA.upper())

