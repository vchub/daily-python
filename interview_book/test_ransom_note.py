# Example: A ransom note can be formed by cutting words out of a magazine to
# form a new sentence. How would you figure out if a ransom note (represented
# as a string) can be formed from a given magazine (string)?

import itertools as it
from collections import Counter
from typing import Dict, List

CharFreq = Dict[str, int]


def is_in(note, magazine: str) -> bool:
    noteCnt = Counter(note)
    magCnt = Counter(magazine)
    return all(noteCnt[k] <= magCnt[k] for k in noteCnt)


def test():
    note = 'i will'
    magazine = 'lil me'
    assert is_in(note, magazine) is False
    assert is_in('i', 'iib') is True
    assert is_in('i will', 'iib willow') is True
    assert is_in('i will you', 'iib willow') is False
