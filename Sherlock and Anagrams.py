def sherlockAndAnagrams(s):
    n = len(s)
    res = 0

    for i in range(1, n):
        cnt = {}

        for j in range(n - i + 1):
            subs = list(s[j:j + i])
            subs.sort()
            subs = ''.join(subs)

            if subs in cnt:
                cnt[subs] += 1
            else:
                cnt[subs] = 1

            res += cnt[subs] - 1

    return res


print(sherlockAndAnagrams("abba"))
print(sherlockAndAnagrams("abcd"))
"""
4
0
"""

print(sherlockAndAnagrams("ifailuhkqq"))
print(sherlockAndAnagrams("kkkk"))
"""
3
10
"""

print(sherlockAndAnagrams("cdcd"))
"""
5
"""
