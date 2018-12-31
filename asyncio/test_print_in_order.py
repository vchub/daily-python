import asyncio
import time
from typing import Callable, List, Tuple

E = int
Res = Tuple[List[int]]
Pred = Callable[[E], bool]


async def worker(xs: List[E], p: Pred, q: Res) -> None:
    for x in xs:
        if p(x):
            q[0].append(x)
        else:
            await asyncio.sleep(1e-9)


async def runner(xs: List[E]) -> List[E]:
    def odd(x):
        return x % 2 != 0

    def even(x):
        return x % 2 == 0

    q: Res = ([], )
    await asyncio.wait([worker(xs, odd, q), worker(xs, even, q)])
    return q[0]


def test():
    xs = [1, 2, 3, 4]
    res = asyncio.run(runner(xs))
    assert res == xs
