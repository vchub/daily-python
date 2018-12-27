import re
from typing import Iterator, NewType, Optional, Sequence


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


def get_user_id() -> Optional[int]:
    pass


def process_user_id(user_id: int):
    pass


##########
# Type
user_id = get_user_id()

# process_user_id(user_id)  # error:

if user_id is not None:
    process_user_id(user_id)  # no error:

E = NewType('E', int)
F = NewType('F', E)


def i(x: E) -> E:
    return x


# j: F = F(3)
# j: F = 3
j: F = F(E(3))

ii = i(j)
ii = i(E(j))

##########
# Seq Covariance
xs: Sequence[E] = []
ys: Sequence[F] = []

xxs = xs
yys = ys

# ys <: xs
yys = xs  # error
xxs = ys

##########
# Function Contravariance


def e(x: E):
    pass


def f(x: F):
    pass


ee = e
ff = f

# e <: f
ff = e
ee = f

# vim:set sw=4 et:
