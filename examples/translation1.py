#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 01:13:52 2019

@author: abhijithneilabraham
"""

from translate import Translator
translator= Translator(to_lang="German")
translation = translator.translate("Good Morning!")
print(translation)