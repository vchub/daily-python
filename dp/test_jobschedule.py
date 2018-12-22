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


def job_seq(js: Jobs) -> Tuple[E]:
    """brute force with caching"""

    def cost(xs: Tuple[E]) -> int:
        return sum(js[x].w for x in xs)

    def remove(js: Tuple[E], e: E) -> Tuple[E]:
        xs = list(js)
        xs.remove(e)
        return tuple(xs)

    @lru_cache(None)
    def loop(rest: Tuple[E], tick: int) -> Tuple[E]:
        res = list((e, ) + loop(remove(rest, e), tick + 1) for e in rest
                   if js[e].end >= tick)
        if not res:
            return ()
        return max(res, key=cost)

    return loop(tuple(js.keys()), 1)


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

    got = job_seq({
        1: Job(2, 100),
        2: Job(1, 19),
        3: Job(2, 27),
        4: Job(1, 25),
        5: Job(3, 15)
    })
    assert sorted(got) == sorted((3, 1, 5))
