#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 01:15:22 2019

@author: abhijithneilabraham
"""

from gensim.summarization.summarizer import summarize
from pattern.web import URL, PDF
pdf2=PDF('forests-10-00219-v2.pdf')
text2=pdf2.string
print(summarize(text2))