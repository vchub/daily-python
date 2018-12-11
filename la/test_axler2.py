import sys

import numpy as np
import numpy.linalg as la


def test2a():
    a = np.array([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1], [0, 0, 0, 1]])
    # print(la.cond(a))
    assert la.cond(a) < 1 / sys.float_info.epsilon
    # la.solve(a,[1,1,1,1])
    # print(sys.float_info.epsilon)

    # for i in range(20):
    #     b = [[3, 1, 4], [2, 3, 5], [5, 9, i]]
    #
    #     if not la.cond(b) < 1 / sys.float_info.epsilon:
    #         print('i= ', i)

    # b = [[3, 1, 4], [2, 3, 5], [5, 9, 14]]
    # b = [[3, 1, 4], [2, 3, 5], [5, 9, 2]]
    # la.inv(b)
    # print(np.array(b, order=False))
