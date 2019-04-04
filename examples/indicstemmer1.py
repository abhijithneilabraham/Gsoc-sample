#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:47:33 2019

@author: abhijithneilabraham
"""

from indicstemmer import getInstance
s = getInstance()
s.stem(u"ഇടുക്കി: മഴ കുറഞ്ഞ പശ്ചാത്തലത്തില്‍ ഇടുക്കി അണക്കെട്ട് മൂന്ന് ദിവസത്തേക്ക്")