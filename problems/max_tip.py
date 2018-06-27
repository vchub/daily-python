# https://practice.geeksforgeeks.org/problems/maximum-tip-calculator/0
import functools


@functools.lru_cache(maxsize=None)
def collect_max(x, y, a, b):
    """ num, num, num, [num], [num] -> num
    maximize the a*Ia + b*Ib
    Ia = [0,1,0...]  |Ia| = x
    Ib = [0,1,0...]  |Ib| = y
    """
    assert len(a) == len(b)
    assert x >= 0
    assert y >= 0

    if len(a) == 0: return 0

    if x == 0: return sum(b)

    if y == 0: return sum(a)

    av = collect_max(x - 1, y, a[1:], b[1:]) + a[0]
    bv = collect_max(x, y - 1, a[1:], b[1:]) + b[0]

    return max(av, bv)


def run():
    cases = int(input())

    for _ in range(cases):
        n, x, y = map(int, input().strip().split(' '))
        a = tuple(map(int, input().strip().split(' ')))
        b = tuple(map(int, input().strip().split(' ')))
        print(collect_max(x, y, a, b))
        # print(n, x, y)
        # print(a)
        # print(b)


if __name__ == '__main__':
    run()
