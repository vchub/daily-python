# lookig for escape for max recursive call limit
# it's 100

import pytest


def rec_gen(i: int) -> int:
    yield i
    yield from rec_gen(i + 1)


def xtest():
    N = int(1e2)
    g = rec_gen(0)
    res = -1
    for i in range(N + 1):
        res = next(g)
    assert res == N
    with pytest.raises(RecursionError):
        for i in range(N * 10):
            res = next(g)
