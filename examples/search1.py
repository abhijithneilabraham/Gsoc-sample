#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 03:36:13 2019

@author: abhijithneilabraham
"""
from pattern.web import Twitter, plaintext
from textblob import TextBlob
twitter = Twitter(language='en') 
for tweet in twitter.search('"Happiness"', cached=False):
    #print(plaintext(tweet.text))
    txt=plaintext(tweet.text)
    blob = TextBlob(txt)
    nn=blob.noun_phrases
    print(nn)
    

