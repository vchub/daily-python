# Given a set of n jobs where each job i has a deadline di >=1 and profit
# pi>=0. Only one job can be scheduled at a time. Each job takes 1 unit of time
# to complete. We earn the profit if and only if the job is completed by its
# deadline. The task is to find the subset of jobs that maximizes profit.

from collections import namedtuple
from functools import lru_cache
from typing import Dict, Iterator, Tuple

E = int
Job = namedtuple('Job', ['end', 'w'])
Jobs = Dict[E, Job]


def job_seq(jobs: Jobs) -> Tuple[E]:
    """brute force with caching"""
    js = jobs.copy()
    js[0] = Job(0, 1)

    def cost(xs: Tuple[E]) -> int:
        return sum(js[x].w for x in xs)

    def children(e: E) -> Iterator[E]:
        # print('children, e: ', e)
        # res = list(k for k, v in js.items() if v.end > js[e].end)
        # print('res: ', res)
        # return res
        return (k for k, v in js.items() if v.end > js[e].end)

    def p(x):
        print('x: ', x)
        return x

    @lru_cache(None)
    def loop(e: E) -> Tuple[E]:
        try:
            # return max((p((e, ) + loop(c)) for c in children(e)), key=cost)
            return max(((e, ) + loop(c) for c in children(e)), key=cost)
        except ValueError as err:
            return (e, )

    return p(loop(0)[1:])


def test():
    js = {1: Job(1, 1), 2: Job(1, 2)}
    assert job_seq(js) == (2, )
    assert job_seq({
        1: Job(4, 20),
        2: Job(1, 10),
        3: Job(1, 40),
        4: Job(1, 30)
    }) == (3, 1)
    assert job_seq({
        1: Job(4, 20),
        2: Job(1, 10),
        3: Job(1, 40),
        4: Job(1, 30)
    }) == (3, 1)

    assert job_seq({
        1: Job(2, 100),
        2: Job(1, 19),
        3: Job(2, 27),
        4: Job(1, 25),
        5: Job(3, 15)
    }) == (3, 1, 5)
