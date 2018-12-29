# Stackless recursive ping-pong

import time
from collections import deque

import pytest

_registry = {}
_msg_queue = deque()


def send(name, msg):
    _msg_queue.append((name, msg))


def run():
    while _msg_queue:
        name, msg = _msg_queue.popleft()
        _registry[name].send(msg)


def actor(fn):
    def wrapper(*args, **kwargs):
        gen = fn(*args, **kwargs)
        next(gen)
        _registry[fn.__name__] = gen
        return gen

    return wrapper


@actor
def ping():
    while True:
        n = yield
        print('ping ', n)
        send('pong', n + 1)
        if n > 10:
            return


@actor
def pong():
    while True:
        n = yield
        print('pong ', n)
        send('ping', n + 1)
        if n > 10:
            return


def test():
    with pytest.raises(StopIteration):
        ping()
        pong()
        send('ping', 0)
        run()
