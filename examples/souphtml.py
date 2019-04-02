#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:05:35 2019

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
response = urllib.request.urlopen('https://www.facebook.com/SachinTendulkar/')
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
for link in soup.find_all('img'):
    print(link.get('href'))
    
    