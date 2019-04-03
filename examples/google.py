#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 00:47:17 2019

@author: abhijithneilabraham
"""
from pattern.web import Twitter

s = "C'est un lapin, lapin de bois. Quoi? Un cadeau."
g = Google()
print(g.translate(s, input='fr', output='en', cached=False))
print(g.identify(s))