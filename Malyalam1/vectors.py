#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:29:58 2019

@author: abhijithneilabraham
"""

from typing import List
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory
import math


Vector = List[float]

def l2_len(v: Vector) -> float:
    return math.sqrt(sum([x*x for x in v]))

def dot(v1: Vector, v2: Vector) -> float:
    assert len(v1) == len(v2)
    return sum([x*y for (x,y) in zip(v1, v2)])

def add(v1: Vector, v2: Vector) -> Vector:
    assert len(v1) == len(v2)
    return [x + y for (x,y) in zip(v1, v2)]

def sub(v1: Vector, v2: Vector) -> Vector:
    assert len(v1) == len(v2)
    return [x - y for (x,y) in zip(v1, v2)]

def normalize(v: Vector) -> Vector:
    factory=IndicNormalizerFactory()
    remove_nuktas=False
   
    normalizer=factory.get_normalizer("hi",remove_nuktas)
    output_text=normalizer.normalize(v)
    return output_text
   

def cosine_similarity_normalized(v1: Vector, v2: Vector) -> float:
    """
    Returns the cosine of the angle between the two vectors.
    Each of the vectors must have length (L2-norm) equal to 1.
    Results range from -1 (very different) to 1 (very similar).
    """
    return dot(v1, v2)