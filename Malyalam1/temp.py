#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 19:17:34 2019

@author: abhijithneilabraham
"""

from indicnlp.normalize.indic_normalize import IndicNormalizerFactory
factory=IndicNormalizerFactory()
remove_nuktas=False
input_text="ഇരിക്കുന്നു  "
normalizer=factory.get_normalizer("hi",remove_nuktas)
output_text=normalizer.normalize(input_text)
print(output_text)