# https://www.codechef.com/wiki/tutorial-dynamic-programming#
# The Longest Increasing Subsequence problem is to find the longest increasing
# subsequence of a given sequence. Given a sequence S= {a1 , a2 , a3, a4,
# ............., an-1, an } we have to find a longest subset such that
# for all j and i,  j<i in the subset aj<ai.


def predecessor(xs, lens, j) -> int:
    """find the biggest k, that k < j && a[k]<a[j]
    return lens[k]
    """
    ls = [lens[k] for k in range(j - 1, -1, -1) if xs[k] < xs[j]]
    return max(ls) if ls else 0


def longIncSubseq(xs) -> int:
    N = len(xs)
    # lens[i] is longest subsequence ending with xs[i]
    lens = [1] * N
    for j in range(N):
        lens[j] += predecessor(xs, lens, j)
    return max(lens)


def test_longIncSubseq():
    assert longIncSubseq([1]) == 1
    assert longIncSubseq([1, 1, 2]) == 2
    assert longIncSubseq([1, 1, 2, 0, 3, 1]) == 3
    assert longIncSubseq([1, 2, 0, 3]) == 3
    assert longIncSubseq([1, 2, -1, 3, 0, 0, 1, 2, 0]) == 4
