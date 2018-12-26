import itertools as it
import threading
import time
from collections import deque
from dataclasses import dataclass
from typing import Callable, Deque, Iterator, List


@dataclass
class Frame:
    n: int
    s: str


def gen_cat(sources: List[Iterator]) -> Iterator[Frame]:
    for s in sources:
        yield from s


def sendto_queue(source: Iterator, q: Deque[Frame]) -> None:
    for x in source:
        q.append(x)
    q.append(StopIteration)


def genfrom_queue(q: Deque[Frame]) -> Iterator[Frame]:
    while True:
        x = q.popleft()
        if x is StopIteration:
            break
        yield x


def filter_queue(q: Deque[Frame], pred: Callable[[Frame], bool],
                 acc: List[Frame]) -> None:
    frames = genfrom_queue(q)
    acc[0] = (x for x in frames if pred(x))


def run_th(acc: Iterator) -> None:
    frame_sources = [(Frame(i, f's: {i}') for i in range(5)),
                     (Frame(i, f's: {i}') for i in range(5, 10))]
    frames = gen_cat(frame_sources)
    q: Deque = deque()

    def odd(x: Frame) -> bool:
        return x.n % 2 == 0

    t1 = threading.Thread(target=sendto_queue, args=(frames, q))
    t2 = threading.Thread(target=filter_queue, args=(q, odd, acc))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def test0():
    acc = [None]
    run_th(acc)
    got = list(acc[0])
    assert len(got) == 5
    # print(got)
