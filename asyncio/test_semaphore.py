# https://tutorialedge.net/python/concurrency/python-asyncio-semaphores-tutorial/

import asyncio
import time
from typing import Callable, List

import pytest


async def myWorker(semaphore):
    await semaphore.acquire()
    print("Successfully acquired the semaphore")
    await asyncio.sleep(.0001)
    print("Releasing Semaphore")
    semaphore.release()


# async def main(loop):
async def main():
    mySemaphore = asyncio.Semaphore(value=2)
    await asyncio.wait(
        [myWorker(mySemaphore),
         myWorker(mySemaphore),
         myWorker(mySemaphore)])
    print("Main Coroutine")


def xtest():
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main(loop))
    # print("All Workers Completed")
    # loop.close()
    asyncio.run(main())
    print("All Workers Completed")


# one worker print odd, another even numbers.
# order of printed numbers (or created array) should be kept (stable sharing)


async def worker(xs: List[int], pred: Callable[[int], bool],
                 res: List[List[int]], semaphore: asyncio.Semaphore) -> None:
    for x in xs:
        await semaphore.acquire()
        if pred(x):
            res[0].append(x)
        semaphore.release()
        await asyncio.sleep(0.000000001)


async def runner(xs: List[int]) -> List[int]:
    def odd(x):
        return x % 2 != 0

    def even(x):
        return x % 2 == 0

    res: List[List[int]] = [[]]
    sm = asyncio.Semaphore(value=1)
    await asyncio.wait([worker(xs, even, res, sm), worker(xs, odd, res, sm)])
    return res[0]


def test_worker():
    xs = [1, 3, 2, 4, 5]
    res = asyncio.run(runner(xs))
    assert res == xs


def nat_recur(start: int, aim: int) -> int:
    if start == aim:
        return start
    return nat_recur(start + 1, aim)


def nat_async(start: int, aim: int) -> int:
    async def loop(start: int, aim: int) -> int:
        if start == aim:
            return start
        res = await loop(start + 1, aim)
        return res

    res = asyncio.run(loop(start, aim))
    return res


def test_nat_async():
    assert nat_async(1, 10) == 10
    with pytest.raises(RecursionError):
        assert nat_async(1, 1000) == 10


def test_nat_recur():
    assert nat_recur(1, 10) == 10
    with pytest.raises(RecursionError):
        nat_recur(1, 1000)
