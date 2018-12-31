from dataclasses import dataclass
from functools import lru_cache, partial
from typing import List, Set


@dataclass
class Node:
    w: int
    c: int


SI = Set[int]
WC = List[Node]


def _weigth(wc: WC, si: SI) -> int:
    return sum(wc[i].w for i in si)


def _cost(wc: WC, si: SI) -> int:
    return sum(wc[i].c for i in si)


#  TODO: change algo to use m(i, w) = max( m(i-1, w), m(i-1,w-w[i]) + v[i] )
#  <03-01-19> #
# https://en.wikipedia.org/wiki/Knapsack_problem
def knapsack(wc: WC, maxweight: int) -> SI:
    """maximize cost of knapsack in constrained maxweight"""

    cost = partial(_cost, wc)
    weigth = partial(_weigth, wc)

    def weigth_of(i):
        return wc[i].w

    # @lru_cache(maxsize=None)
    def S(si: SI, maxweight: int) -> SI:
        if maxweight <= 0:
            return set()
        if weigth(si) <= maxweight:
            return si

        res: SI = set()
        maxcost = 0
        for i in si:
            s = S(si.difference({i}), maxweight - weigth_of(i))
            s.add(i)
            if weigth(s) <= maxweight and cost(s) > maxcost:
                maxcost = cost(s)
                res = s
        return res

    return S(set(range(len(wc))), maxweight)


def towc(s: str) -> WC:
    return list(
        Node(int(w), int(c)) for w, c in (wc.split(',') for wc in s.split()))


def test():
    wc = [Node(1, 2)]
    got = knapsack(wc, 1)
    cost = partial(_cost, wc)
    weigth = partial(_weigth, wc)
    assert got == {0} and weigth(got) == 1 and cost(got) == 2

    wc = towc('1,1 2,3 1,3')
    got = knapsack(wc, 2)
    cost = partial(_cost, wc)
    weigth = partial(_weigth, wc)
    assert got == {0, 2} and weigth(got) == 2 and cost(got) == 4

    wc = towc('1,1 2,4 1,3')
    got = knapsack(wc, 2)
    cost = partial(_cost, wc)
    weigth = partial(_weigth, wc)
    assert got == {0, 2} and weigth(got) == 2 and cost(got) == 4

    # print('lru_cache(): ', reduce.cache_info())


# set tabstop=4
