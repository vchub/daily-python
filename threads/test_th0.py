import threading
import time


def th0(xs):
    """docstring for th0"""
    time.sleep(0.05)
    print("\nin th0")
    for i, _ in enumerate(xs):
        xs[i] *= 2
    # return xs


def xtest_th0():
    """docstring for test_th0"""
    xs = [1]

    def f():
        th0(xs)
        print(f"xs={xs}")

    threading.Thread(target=f).start()
    print(f"xs={xs}")

    assert 0 == 0
