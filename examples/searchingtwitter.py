#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:40:32 2019

@author: abhijithneilabraham
"""

from pattern.web import Twitter, plaintext
twitter = Twitter(language='en') 
for tweet in twitter.search('"Happiness"', cached=False):
    print(plaintext(tweet.text))