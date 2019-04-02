#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:14:27 2019

@author: abhijithneilabraham
"""
'''
from pattern.web import URL, extension
  
url = URL('http://www.clips.ua.ac.be/media/pattern_schema.gif')
f = open('test' + extension(url.page), 'wb') # save as test.gif
f.write(url.download())
f.close()
'''
from bs4 import BeautifulSoup
import urllib.request
import re

url = URL('http://imgur.com')
soup = BeautifulSoup(html_page,features="lxml")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
    #f = open('test' + extension(url.page), 'wb') # save as test.gif
    #f.write(url.download())
    #f.close()
    print(images)
    

