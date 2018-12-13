# 8 queen problem

import functools


def queen_num(n: int) -> int:
    """n - board size"""
    # a list of filled positions (row, col)
    filled: tuple = ()

    @functools.lru_cache(None)
    def loop(filled, row) -> int:
        """row - next row to try a queen
            return number of possible states
        """
        if row >= n:
            return 1
        res = 0
        for col in range(n):
            if can_add(filled, row, col):
                res += loop(filled + ((row, col), ), row + 1)
        return res

    return loop(filled, 0)


def can_add(filled, row, col) -> bool:
    for i, j in filled:
        if col == j or abs(i - row) == abs(j - col):
            return False
    return True


def test_q():
    assert queen_num(1) == 1
    assert queen_num(2) == 0
    assert queen_num(3) == 0
    assert queen_num(4) == 2
    assert queen_num(5) == 10
    assert queen_num(8) == 92
