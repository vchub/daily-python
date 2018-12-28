# having [1,3,2,5,1,6], Thread1 print odd num, Thread2 print even num,
# resulting string (print) shoud have the save order as original list
# instead of print, let's create new list

import threading
import time
from typing import Callable, List


def run(xs: List[int]) -> List[int]:
    xs_lock = threading.Lock()

    res: List[int] = []

    def even(x):
        return x % 2 == 0

    def odd(x):
        return x % 2 != 0

    threads = [
        threading.Thread(target=pr, args=[xs, res, even, xs_lock]),
        threading.Thread(target=pr, args=[xs, res, odd, xs_lock])
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return res


def pr(xs: List[int], res: List[int], pred: Callable[[int], bool], xs_lock):
    for x in xs:
        xs_lock.acquire()
        if pred(x):
            res.append(x)
        xs_lock.release()
        time.sleep(0.0005)


def xtest():
    assert run([1, 2, 3]) == [1, 2, 3]
    assert run([1, 2, 3]) is not [1, 2, 3]

    assert run([1, 1, 2, 3, 4, 4]) == [1, 1, 2, 3, 4, 4]
