#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:29:57 2019

@author: abhijithneilabraham
"""
import math
import vectors as v
import re
from typing import List,Tuple,Iterable,Set
Vector=List[float]
class Word:
    def __init__(self,text=str,vector=Vector)->None:
        self.text=text
        self.vector=vector
def vector_len(v: Vector) -> float:
    return math.sqrt(sum([x*x for x in v]))

def dot_product(v1: Vector, v2: Vector) -> float:
    assert len(v1) == len(v2)
    return sum([x*y for (x,y) in zip(v1, v2)])

def cosine_similarity(v1: Vector, v2: Vector) -> float:
    """
    Returns the cosine of the angle between the two vectors.
    Results range from -1 (very different) to 1 (very similar).
    """
    return dot_product(v1, v2) / (vector_len(v1) * vector_len(v2))
def sorted_by_similarity(words: List[Word], base_vector: Vector) -> List[Tuple[float, Word]]:
    """Returns words sorted by cosine distance to a given vector, most similar first"""
    words_with_distance = [(cosine_similarity(base_vector, w.vector), w) for w in words]
    # We want cosine similarity to be as large as possible (close to 1)
    return sorted(words_with_distance, key=lambda t: t[0], reverse=True)

    
def find_word(words: List[Word], text: str) -> Word:
    return next(w for w in words if text == w.text)
def print_related(words: List[Word], text: str) -> None:
    base_word = find_word(text, words)
    sorted_words = [
        word.text for (dist, word) in
            sorted_by_similarity(words, base_word.vector)
            if word.text.lower() != base_word.text.lower()
        ]
    print(', '.join(sorted_words[:7]))
def load_words_raw(file_path: str) -> List[Word]:
    """Load the file as-is, without doing any validation or cleanup."""
    def parse_line(line: str, frequency: int) -> Word:
        tokens = line.split()
        word = tokens[0]
        vector = v.normalize([float(x) for x in tokens[1:]])
        return Word(word, vector, frequency) 
ignore_char_regex = re.compile("[\W_]")
def remove_duplicates(words: List[Word]) -> List[Word]:
    seen_words: Set[str] = set()
    unique_words: List[Word] = []
    for w in words:
        canonical = ignore_char_regex.sub("", w.text)
        if not canonical in seen_words:
            seen_words.add(canonical)
            # Keep the original ordering
            unique_words.append(w)
    return unique_words
is_valid_word = re.compile("^[^\W_].*[^\W_]$")

def remove_stop_words(words: List[Word]) -> List[Word]:
    return [w for w in words if (len(w.text) > 1 and is_valid_word.match(w.text))]
def load_words(file_path: str) -> List[Word]:
    """Load and cleanup the data."""
    
    words = load_words_raw(file_path)
   
    
    words = remove_stop_words(words)

    
    words = remove_duplicates(words)
   
    return words

words = load_words('/Users/abhijithneilabraham/Documents/wiki.ml.vec')

