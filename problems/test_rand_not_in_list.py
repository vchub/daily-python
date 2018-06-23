# This question was asked by Google.
#
# Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

import random


def gen_not(n, xs):
    s = set(range(n)).difference(set(xs))

    return random.choice(list(s))


# def test0():
#     for i in range(20):
#         assert gen_not(5, [1, 2, 3]) not in [1, 2, 3]
