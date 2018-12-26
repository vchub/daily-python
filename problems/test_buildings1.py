# You are given an array representing the heights of neighboring buildings on a
# city street, from east to west. The city assessor would like you to write an
# algorithm that returns how many of these buildings have a view of the setting
# sun, in order to properly value the street.  For example, given the array [3,
# 7, 8, 3, 6, 1], you should return 3, since the top floors of the buildings
# with heights 8, 6, and 1 all have an unobstructed view to the west.
from typing import List


def new_max_right(xs: List[int]) -> int:
    if not xs:
        return 0
    t = 1
    m = xs[-1]
    for i in range(len(xs) - 2, -1, -1):
        if xs[i] > m:
            m = xs[i]
            t += 1
    return t


def test():
    assert new_max_right([1]) == 1
    assert new_max_right([2, 1]) == 2
    assert new_max_right([3, 7, 8, 3, 6, 1]) == 3
