#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 01:15:22 2019

@author: abhijithneilabraham
"""

from gensim.summarization.summarizer import summarize
from pattern.web import URL, PDF
url = URL('http://www.clips.ua.ac.be/sites/default/files/ctrs-002_0.pdf')
pdf = PDF(url.download())   
text = pdf.string
print(text)
print(summarize(text))