# The 24 game is played as follows. You are given a list of four integers, each
# between 1 and 9, in a fixed order. By placing the operators +, -, *, and /
# between the numbers, and grouping them with parentheses, determine whether it
# is possible to reach the value 24.  For example, given the input [5, 2, 7,
# 8], you should return True, since (5 * 2 - 7) * 8 = 24.

import operator
from functools import lru_cache

# import pdb
# pdb.set_trace()

ops = (operator.mul, operator.add, operator.sub, operator.truediv)

C = 24


@lru_cache(maxsize=None)
def M(x: tuple) -> bool:
    if len(x) < 2:
        return x[0] == C
    for i in range(len(x) - 1):
        for fn in ops:
            xs = x[:i] + (fn(x[i], x[i + 1]), ) + x[i + 2:]
            # breakpoint()
            if M(xs):
                return True
    return False


def test():
    assert M((24, )) is True
    assert M((12, 12)) is True
    assert M((12, 2, 6)) is True
    assert M((5, 2, 7, 8)) is True
