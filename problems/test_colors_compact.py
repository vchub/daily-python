# On a mysterious island there are creatures known as Quxes which come in three
# colors: red, green, and blue. One power of the Qux is that if two of them are
# standing next to each other, they can transform into a single creature of the
# third color.
#
# Given N Quxes standing in a line, determine the smallest number of them
# remaining after any possible sequence of such transformations.
#
# For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end
# up with a single Qux through the following steps:

#         Arrangement       |   Change
# ----------------------------------------
# ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
# ['B', 'B', 'G', 'B']      | (B, G) -> R
# ['B', 'R', 'B']           | (R, B) -> G
# ['B', 'G']                | (B, G) -> R
# ['R']                     |

from functools import lru_cache
from typing import Tuple

# T = Tuple[str, ...]
T = str


def done(xs: T) -> bool:
    return len(xs) == 0 or all(xs[0] == x for x in xs)


def comp(xs: T) -> T:
    colors = set('rgb')
    t = set(xs)
    if len(t) <= 1:
        return xs
    return ''.join(colors.difference(t))


@lru_cache(None)
def reduce(xs: T) -> int:
    if done(xs):
        return len(xs)
    children = (xs[:i] + comp(xs[i:i + 2]) + xs[i + 2:]
                for i in range(len(xs) - 1))
    # print(children)
    res = min(reduce(ch) for ch in children if len(ch) < len(xs))
    return res


def test_reduce():
    assert reduce('') == 0
    assert reduce('rg') == 1
    assert reduce('rr') == 2
    assert reduce('rgb') == 2
    assert reduce('rgbr') == 1
    assert reduce('rgbgb') == 1
    assert reduce('rgbgbbgrbgr') == 1
    # assert reduce('rrgbgbbgrbgrgbgbbgrbgr') == 2
    # print('lru_cache(): ', reduce.cache_info())


def test_done():
    assert done('') is True
    assert done('a') is True
    assert done('aaba') is False
