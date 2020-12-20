from collections import Counter


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    map1 = Counter(a)
    map2 = Counter(b)

    diff_cnt = 0
    for key in map2.keys():
        if key not in map1:
            diff_cnt += map2[key]
        else:
            diff_cnt += max(0, map2[key] - map1[key])

    for key in map1.keys():
        if key not in map2:
            diff_cnt += map1[key]
        else:
            diff_cnt += max(0, map1[key] - map2[key])

    return diff_cnt


print(makeAnagram("cde", "abc"))
"""
4
"""

print(makeAnagram("showman", "woman"))
"""
2
"""

print(makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"))
"""
30
"""
