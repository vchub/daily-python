# Example: Given an array of distinct integer values, count the number of pairs
# of integers that have difference k. For example, given the array {1, 7, 5, 9,
# 2, 12, 3} and the difference k = 2, there are four pairs with difference 2:
# (1, 3), (3, 5), (5, 7), (7, 9) .

from typing import List, Optional, Tuple


def diff2(xs: List[int]) -> List[Tuple[int, int]]:
    xs = sorted(xs)

    def add(i: int) -> Optional[Tuple[int, int]]:
        if xs[i + 1] - xs[i] == 2:
            return (xs[i], xs[i + 1])
        elif xs[i + 2] - xs[i] == 2:
            return (xs[i], xs[i + 2])
        return None

    res = list(filter(None, (add(i) for i in range(len(xs) - 2))))

    i = len(xs) - 2
    if xs[i + 1] - xs[i] == 2:
        res.append((xs[i], xs[i + 1]))
    return res


def diff2_set(ys: List[int]) -> List[Tuple[int, int]]:
    xs = set(ys)
    res = list((x, x + 2) for x in xs if x + 2 in xs)
    return res


def test():
    assert diff2([1, 2, 3]) == [(1, 3)]
    assert diff2([1, 7, 5, 9, 2, 12, 3]) == [(1, 3), (3, 5), (5, 7), (7, 9)]
    assert diff2_set([1, 2, 3]) == [(1, 3)]
    assert diff2_set([1, 7, 5, 9, 2, 12, 3]) == [(1, 3), (3, 5), (5, 7), (7,
                                                                          9)]
