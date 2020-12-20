from collections import defaultdict


def countTriplets(arr, r):
    m1, m2 = defaultdict(int), defaultdict(int)
    triplets = 0

    for i in reversed(arr):
        if i * r in m2:
            triplets += m2[i * r]

        if i * r in m1:
            m2[i] += m1[i * r]

        m1[i] += 1

    
    return triplets


print(countTriplets([1, 2, 2, 4], 2))
"""
2
(0, 1, 3)
(0, 2, 3)
"""

print(countTriplets([1, 3, 9, 9, 27, 81], 3))
"""
6
(0, 1, 2)
(0, 1, 3)
(1, 2, 4)
(1, 3, 4)
(2, 4, 5)
(3, 4, 5)
"""

print(countTriplets([1, 5, 5, 25, 125], 5))
"""
4
(0, 1, 3)
(0, 2, 3)
(1, 3, 4)
(2, 3, 4)
"""
