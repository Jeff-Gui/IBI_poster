# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:11:03 2019

@author: Wyxx
"""

from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

DNA=input('please enter a sequence of DNA:')
DNA=Seq.Seq(DNA,IUPAC.unambiguous_dna)

mRNA=DNA.transcribe()
protein=mRNA.translate()
print(protein)