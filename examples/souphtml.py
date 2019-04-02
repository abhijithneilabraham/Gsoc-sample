#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:05:35 2019

@author: abhijithneilabraham
"""
from bs4 import BeautifulSoup
import urllib.request
response = urllib.request.urlopen('https://imgur.com/')
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())