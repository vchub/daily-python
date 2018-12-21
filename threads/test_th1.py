import json
import multiprocessing
import os
import threading
import time

import requests


def countDown(n: int) -> int:
    """TODO: Docstring for count.

    :n : int: TODO
    :returns: TODO

    """
    # time.sleep(0.05)
    while n > 0:
        n -= 1
    return n


def th0(xs):
    """docstring for th0"""
    time.sleep(0.05)
    print("\nin th0")
    for i, _ in enumerate(xs):
        xs[i] *= 2
    # return xs


def wFile(fname: str, n: int):
    xs = [{'a': 1}] * n
    with open(fname, 'w') as f:
        f.write(json.dumps(xs))


def clean(dname: str):
    for f in os.listdir(dname):
        _, fext = os.path.splitext(f)
        if fext == '.json':
            os.remove(f)


def multiWrite(n: int) -> float:
    threads = [
        threading.Thread(target=wFile, args=[f"{i}.json", n]) for i in range(n)
    ]
    start = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    return end - start


def multiWriteProcess(n: int) -> float:
    args = [[f"{i}.json", n] for i in range(n)]
    start = time.time()
    with multiprocessing.Pool(n) as p:
        p.imap(wFile, args)
    end = time.time()
    return end - start


def xtest_multiWriteProcess():
    t1 = multiWrite(1)
    print(f"one Thread time: {t1}")
    N = 2

    td = multiWrite(N)
    ratio = td / t1
    print(f"Thread time: {td}, ratio: {ratio}")
    clean('.')

    tp = multiWriteProcess(N)
    ratio = tp / t1
    print(f"multiProcess time: {tp}, ratio: {ratio}")
    clean('.')


def multiProcess(N: int):
    pool = multiprocessing.Pool(processes=2)
    start = time.time()
    pool.apply_async(countDown, [N])
    pool.apply_async(countDown, [N])
    pool.close()
    pool.join()
    end = time.time()
    # print("total time: %f".format(end - start))
    print("multiProcess time: %f" % (end - start))


# def multiThread(N: int):
#     t1 = threading.Thread(target=countDown, args=[N])
#     t2 = threading.Thread(target=countDown, args=[N])
#     start = time.time()
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time.time()
#     # print("total time: %f".format(end - start))
#     print("total time: %f" % (end - start))

#
#
# def test_th0():
#     N = 1000000
#     multiThread(N)
#     multiProcess(N)
#     assert 0 == 0


def multiThrGetter(url: str, N: int):
    threads = [
        threading.Thread(target=requests.get, args=[url]) for _ in range(N)
    ]
    start = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    return end - start


def xtest_multiThrGetter():
    url = 'https://google.com'
    t1 = multiThrGetter(url, 1)
    print(f"one Thread time: {t1}")
    N = 20
    t2 = multiThrGetter(url, N)
    ratio = t2 / t1
    print(f"{N} Thread time: {t2}, ratio: {ratio}")
