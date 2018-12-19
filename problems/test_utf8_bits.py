# https://mail.google.com/mail/u/0/#inbox/FMfcgxwBTjvMnDRsbPwRWXrpnjFVSCph

# UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.
# For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. The rules for mapping characters are as follows:
#
# For a single-byte character, the first bit must be zero.
# For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.
# Visually, this can be represented as follows.
#
#  Bytes   |           Byte format
# -----------------------------------------------
#    1     | 0xxxxxxx
#    2     | 110xxxxx 10xxxxxx
#    3     | 1110xxxx 10xxxxxx 10xxxxxx
#    4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
# Write a program that takes in an array of integers representing byte
# values, and returns whether it is a valid UTF-8 encoding.


def valid_data(xs: list) -> bool:
    return all([x >> 6 == 0b10 for x in xs])


def chunk(xs: list) -> int:
    i = 0
    c = xs[i]
    if c >> 7 == 0:
        return 1
    elif c >> 5 == 0b110 and valid_data(xs[i + 1:i + 2]):
        return 2
    elif c >> 4 == 0b1110 and valid_data(xs[i + 1:i + 3]):
        return 3
    elif c >> 3 == 0b11110 and valid_data(xs[i + 1:i + 4]):
        return 4
    else:
        return 0


def valid_utf8(xs: list) -> bool:
    i = 0
    while i < len(xs):
        j = chunk(xs)
        if j == 0:
            return False
        i += j
    return i == len(xs)


def s_to_ia(s: str) -> list:
    return [int(x, 2) for x in s.split()]


def test_valid_utf8():
    # s = '01111111'
    # print(s_to_ia(s))
    assert valid_utf8(s_to_ia('01111111'))
    assert not valid_utf8(s_to_ia('11111111'))
    assert not valid_utf8(s_to_ia('11011111'))
    assert valid_utf8(s_to_ia('11011111 10011111'))
    assert not valid_utf8(s_to_ia('11011111 11011111'))
    assert valid_utf8(s_to_ia('11100111 10011111 10011111'))
    assert valid_utf8(s_to_ia('11110111 10011111 10011111 10011111'))
    assert valid_utf8(
        s_to_ia('11110111 10011111 10011111 10011111 \
                              11110111 10011111 10011111 10011111'))
