# The edit distance between two words—sometimes also called the Levenshtein distance—is the minimum number of letter insertions, letter deletions, and letter substitutions required to transform one word into another. For example, the edit distance between FOOD and MONEY is at most four:
#     FOOD → MOOD → MON∧D → MONED → MONEY:

import timeit
from functools import lru_cache

from problems.test_min_edit_dist import edit_dist_dp


@lru_cache(None)
def mED(x, y: str) -> int:
    if len(x) is 0:
        return len(y)
    if len(y) is 0:
        return len(x)
    if x[-1] == y[-1]:
        return mED(x[:-1], y[:-1])
    else:
        return 1 + min(
            # insert
            mED(x + y[-1], y),
            # delete
            mED(x[:-1], y),
            # edit
            mED(x[:-1] + y[-1], y),
        )


def test_mED():
    assert mED('', '') is 0
    assert mED('x', '') is 1
    assert mED('', 'x') is 1
    assert mED('x', 'x') is 0
    assert mED('xy', 'x') is 1
    assert mED('food', 'money') is 4
    assert mED('sunday', 'saturday') == 3

    x, y = "skfkfsundayabc", "saturdayefg"
    tTb = timeit.timeit(lambda: edit_dist_dp(x, y), number=1)
    tmEd = timeit.timeit(lambda: mED(x, y), number=1)
    print(f'mED time: {tmEd}, edit_dist_dp time: {tTb}')
    print('mED.lru_cache(): ', mED.cache_info())
