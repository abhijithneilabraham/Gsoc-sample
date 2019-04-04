#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:02:02 2019

@author: abhijithneilabraham
"""

from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
text = u"Quelle belle matinée"
blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
print(blob.tags)
print(blob.sentiment)