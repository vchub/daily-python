import bz2
import gzip
import os
from pathlib import Path
from typing import Iterator


def sum_log1(path):
    def parse(l: str) -> int:
        x = l.rsplit(None, 1)[1]
        return int(x) if x.isdigit() else 0

    with open(path, 'r') as f:
        return sum(parse(l) for l in f)


def sum_log(path, fn_open):
    # print(path, fn_open)
    with fn_open(path, 'rt') as f:
        colunm = (l.rsplit(None, 1)[1] for l in f)
        return sum(int(x) for x in colunm if x.isdigit())


def sum_log_walk(path):
    tbl = {'gz': gzip.open, 'bz2': bz2.open, 'log': open}

    logs = (os.path.join(root, fname) for root, dirs, files in os.walk(path)
            for fname in files if 'access-log' in fname)
    return sum(
        sum_log(log, tbl.get(log.rsplit('.', 1)[1], open)) for log in logs)


def xtest_sum_log():
    log = os.path.join(
        os.path.dirname(__file__), '../generators/examples/access-log')
    print('sum_log: %d' % sum_log(log, open))

    root_dir = os.path.join(
        os.path.dirname(__file__), '../generators/examples')
    print('sum_log_walk: %d' % sum_log_walk(root_dir))


def gen_open(paths: Iterator[Path]) -> Iterator:
    for p in paths:
        if p.suffix is '.gz':
            yield gzip.open(p, 'rt')
        elif p.suffix is '.bz2':
            yield bz2.open(p, 'rt')
        else:
            yield open(p, 'rt')


def gen_cat(sources: Iterator) -> Iterator:
    for s in sources:
        yield from s
