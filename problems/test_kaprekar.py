# The number 6174 is known as Kaprekar's contant, after the mathematician who
# discovered an associated property: for all four-digit numbers with at least
# two distinct digits, repeatedly applying a simple procedure eventually
# results in this value. The procedure is as follows:
#
# For a given input x, create two new numbers that consist of the digits in x
# in ascending and descending order.  Subtract the smaller number from the
# larger number.  For example, this algorithm terminates in three steps when
# starting from 1234:
#
# 4321 - 1234 = 3087
# 8730 - 0378 = 8352
# 8532 - 2358 = 6174
# Write a function that returns how many steps this will take for a given input
# N.


def kapr_n(x: int) -> int:
    K = 6174
    if x == K:
        return 0

    def nxt(x: int) -> int:
        s = sorted(str(x))
        return int(''.join(reversed(s))) - int(''.join(s))

    nx = nxt(x)
    i = 1
    while nx != K:
        nx = nxt(nx)
        i += 1
    return i


def test():
    assert kapr_n(6174) == 0
    assert kapr_n(1234) == 3


# Excerpt From: David Beazley and Brian K. Jones. “Python Cookbook.” Apple
# Books.


def xtest_infinite_loop_as_iter():
    # import sys
    f = open('/etc/passwd')
    for chunk in iter(lambda: f.read(10), ''):
        # n = sys.stdout.write(chunk)
        # print(f'chunk {chunk}')
        pass
