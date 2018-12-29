import itertools as it
from typing import List


def substr_ind(a: str, b: str) -> List[int]:
    A = sorted(a)

    # frame = sorted(b[:len(A)])

    def nxt(i: int) -> List[str]:
        # nonlocal frame
        # print(frame, b, i, b[i - 1:i + 1])
        # frame = rm(frame, b[i - 1])
        # print(frame)
        # frame = ins(frame, b[i + len(a) - 1])

        return sorted(b[i:i + len(a)])

    return list(i for i in range(len(b) - len(a) + 1) if nxt(i) == A)


def rm(xs: List[str], c: str) -> List[str]:
    """xs is sorted"""
    i = xs.index(c)
    return xs[:i] + xs[i + 1:]


def ins(xs: List[str], c: str) -> List[str]:
    front = list(it.takewhile(lambda x: x < c, xs))
    return front + [c] + xs[len(front) + 1:]


def test():
    assert substr_ind('a', 'abac') == [0, 2]
    assert substr_ind('ab', 'abacba') == [0, 1, 4]
    assert substr_ind('ab', 'abacab') == [0, 1, 4]
    assert substr_ind('ab', 'abacaba') == [0, 1, 4, 5]
    assert substr_ind('aba', 'abacaba') == [0, 4]
    assert len(substr_ind('abbc', 'cbabadcbbabbcbabaabccbabc')) == 7
