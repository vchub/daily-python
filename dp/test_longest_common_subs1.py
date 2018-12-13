# A subsequence of a given sequence is the given sequence with just some elements
# left out (order should be from left-to-right, not necessarily consecutive)..
# A common sequence of two sequences X and Y, is a subsequence of both X and Y.A
# longest common subsequence is the one with maximum length. For example,
# if X = {A,B,C,B,D,A,B} and Y = { B,D,C,A,B,A} then the longest common
# subsequence is of length 4 and they are {B,C,B,A} and {B,D,A,B}.

# from typing import Tuple
import functools


@functools.lru_cache(None)
def S(xs, ys: str) -> str:
    if len(xs) == 0 or len(ys) == 0:
        return ''
    if xs[-1] == ys[-1]:
        return S(xs[:-1], ys[:-1]) + xs[-1]
    else:
        return max(S(xs[:-1], ys), S(xs, ys[:-1]), key=len)


def test_S():
    assert S('ab', 'b') == 'b'
    assert S('ab', 'cab') == 'ab'
    assert S('xaxbx', 'cacbc') == 'ab'
    assert S('ABCBDAB', 'BDCABA') == 'BCBA'
    assert S('abcdefglkmxyz', '_____bdfabckyxxxxz') == 'abckxz'
    print('lru_cache(): ', S.cache_info())
