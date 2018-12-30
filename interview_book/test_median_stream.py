# Given an input stream of n integers the task is to insert integers to stream
# and print the median of the new stream formed by each insertion of x to the
# stream.
#
# Example
#
# Flow in stream : 5, 15, 1, 3
# 5 goes to stream --> median 5 (5)
# 15 goes to stream --> median 10 (5, 15)
# 1 goes to stream --> median 5 (5, 15, 1)
# 3 goes to stream --> median 4 (5, 15, 1, 3)

import dataclasses as dt
import fileinput
import heapq
from typing import List, Tuple

E = int


@dt.dataclass
class LR:
    l: List[E] = dt.field(default_factory=list)
    r: List[E] = dt.field(default_factory=list)

    def add(self, x: E) -> None:
        if not self.l:
            self.l.append(-x)
        elif x <= self.floor_median():
            heapq.heappush(self.l, -x)
        else:
            heapq.heappush(self.r, x)
        self.rebalance()

    def rebalance(self) -> None:
        if len(self.l) < len(self.r):
            heapq.heappush(self.l, -1 * heapq.heappop(self.r))
        if len(self.l) > len(self.r) + 1:
            heapq.heappush(self.r, -1 * heapq.heappop(self.l))

    def median(self) -> Tuple[E, E]:
        m = -self.l[0]
        if len(self.l) > len(self.r):
            return m, m
        else:
            return m, self.r[0]

    def floor_median(self) -> E:
        return int(sum(self.median()) / 2)


def run():
    inp = fileinput.input()
    n = int(next(inp))
    lr = LR()
    for i in range(n):
        lr.add(int(next(inp)))
        print(lr.floor_median())


if __name__ == "__main__":
    run()


def median_0(xs: List[int]) -> Tuple[int, int]:
    n = len(xs)
    if n % 2 == 0:
        return xs[int(n / 2) - 1], xs[int(n / 2)]
    else:
        return xs[int(n / 2)], xs[int(n / 2)]


def test():
    xs = [5, 3, 2, 4]
    assert median_0([1]) == (1, 1)
    assert median_0([1, 2]) == (1, 2)
    assert median_0([1, 2, 3]) == (2, 2)

    lr = LR()
    for i, x in enumerate(xs):
        lr.add(x)
        sl = xs[:i + 1]
        # print(lr)
        assert lr.median() == median_0(sorted(sl))
        m = median_0(sorted(sl))
        assert lr.floor_median() == int(sum(m) / 2)


#
