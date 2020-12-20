import itertools as it


def arrayManipulation(n, queries):
    q = it.chain.from_iterable([(a, -k), (b, k)] for a, b, k in queries)
    return max(it.accumulate(-c for _, c in sorted(q)))


print(arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))
