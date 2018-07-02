# https://brilliant.org/practice/rule-of-sum-and-rule-of-product-problem-solving/?p=2

import collections
import itertools as it


def flatten(xxs):
    return [x for sub in xxs for x in sub]


def xtest_card():
    assert flatten([[1, 2], [3, 4]]) == list(range(1, 5))
    assert flatten([[[1, 2], [3, 4]], [[1, 2]]]) == [[1, 2], [3, 4], [1, 2]]
    xs = collections.Counter(
        map(
            sum,
            flatten([
                it.combinations_with_replacement(
                    it.chain([10] * 8, [100] * 5, [500] * 2), i)
                for i in range(1, 1)
            ])))
    print('---- xs: ', xs)
    # assert 10 == len(xs)
