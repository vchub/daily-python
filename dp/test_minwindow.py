# Given a string, find the length of the smallest window that contains every
# distinct character. Characters may appear more than once in the window.
#
# For example, given "jiujitsu", you should return 5, corresponding to the
# final five letters.

from functools import lru_cache
from typing import FrozenSet

V = FrozenSet[str]


def solution(s: str) -> int:
    v = frozenset(s)
    # N = len(v)

    @lru_cache(maxsize=None)
    def w(i: int, v: V) -> int:
        if len(v) == 0:
            return 0
        if i < len(v) - 1:
            return len(s)
        res = min(1 + w(i - 1, v.difference(s[i])), w(i - 1, v))
        return res

    return w(len(s) - 1, v)


def test0():
    assert solution('') == 0
    assert solution('i') == 1
    assert solution('ji') == 2
    assert solution('jij') == 2
    assert solution('djij') == 3
    assert solution('jiujitsu') == 5
    assert solution('jiujitsuju') == 5
