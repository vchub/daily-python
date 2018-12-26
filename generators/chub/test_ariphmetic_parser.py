import re
from typing import Iterator


def tokenize(s: str) -> Iterator[str]:
    pattern = r'[0-9.]+|[()*/+-]'
    return (m.group(0) for m in re.finditer(pattern, s))


def test_tokenize():
    assert list(tokenize('1()')) == list('1()')
    assert list(tokenize('2.0')) == ['2.0']
    assert list(tokenize('-2.0')) == ['-', '2.0']
    assert list(tokenize('1+( 2.0*3333 )')) == '1 + ( 2.0 * 3333 )'.split()


def test_getter():
    import operator as op
    x = (1, 2, 3)
    assert op.itemgetter(1)(x) == 2
    assert op.itemgetter(2)(x) == 3


# vim:set sw=4 et:
