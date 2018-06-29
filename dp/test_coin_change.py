# https://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/<Paste>

import functools


@functools.lru_cache(maxsize=None)
def change(n, coins):
    """n, [int]-> int

    For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1}
    ,{1,1,2},{2,2},{1,3} """

    if n < 0 or len(coins) < 1: return 0

    if n == 0: return 1

    return change(n - coins[0], coins) + change(n, coins[1:])


def run():
    cases = int(input())

    for _ in range(cases):
        # m = int(input().strip())
        input()
        coins = tuple(reversed(tuple(map(int, input().strip().split(' ')))))
        n = int(input().strip())
        print(change(n, coins))


if __name__ == '__main__':
    run()


def xtest_change():
    assert 0 == change(1, ())
    assert 1 == change(1, (1, ))
    assert 2 == change(2, (1, 2))
    assert 4 == change(4, (1, 2, 3))
    print('lru_cache(): ', change.cache_info())
    assert 9253082936723601 == change(300, tuple(reversed(range(1, 300))))
    print('lru_cache(): ', change.cache_info())


tuple(reversed((1, 2, 3)))
