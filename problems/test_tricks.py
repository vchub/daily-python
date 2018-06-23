def test_reverse():
    x = 'abc'
    res = [c for c in x]
    res.reverse()
    # print(res)
    assert ''.join(res) == x[::-1]


def is_anagram(word1, word2):
    """Checks whether the words are anagrams.
    word1: string
    word2: string

    returns: boolean
    """

    return word1 == word2[::-1]


def test_anagram():
    assert is_anagram('ab', 'ba')
    assert is_anagram('abc', 'cba')
    assert not is_anagram('aba', 'cba')


def test_transpose():
    mat = [[1, 2, 3], [4, 5, 6]]
    got = list(zip(*mat))
    assert got == [(1, 4), (2, 5), (3, 6)]
