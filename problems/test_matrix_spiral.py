# https://mail.google.com/mail/u/0/#inbox/16374014fc038510
# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
#
# For example, given the following matrix:
#
# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]
# You should print out the following:
#
# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# ....

import numpy as np

a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20]]

ar = np.array(a)


def get_range(a, x1, y1, x2, y2):
    res = []

    if x1 < x2:
        for i in range(x1, x2 + 1, 1):
            res.append(a[i][y1])
    elif x2 < x1:

        for i in range(x1, x2 - 1, -1):
            res.append(a[i][y1])
    elif y1 < y2:
        for i in range(y1, y2 + 1, 1):
            res.append(a[x1][i])
    else:
        for i in range(y1, y2 - 1, -1):
            res.append(a[x1][i])

    return res


def cycle(a, x1, y1, x2, y2):
    """ point 1 and 2 on main diagonal"""

    if x1 > x2 or y1 > y2:
        return []

    res = []
    res.append((get_range(a, x1, y1, x1, y2)))
    res.append((get_range(a, x1 + 1, y2, x2, y2)))
    res.append((get_range(a, x2, y2 - 1, x2, y1)))
    res.append((get_range(a, x2 - 1, y1, x1 + 1, y1)))

    return res


# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]


def solutioin(a):
    x1, y1 = 0, 0
    x2, y2 = len(a) - 1, len(a[0]) - 1
    got = cycle(a, x1, y1, x2, y2)
    res = []

    while got != []:
        res.extend(got)
        # print(res)
        x1 += 1
        y1 += 1
        x2 -= 1
        y2 -= 1
        got = cycle(a, x1, y1, x2, y2)

    # flatten
    res = [x for subl in res for x in subl]

    return res


# print(solutioin(a))

a = []
a.extend([3, 3])
a.extend([5, 3])
a
