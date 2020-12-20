# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    counter = 0

    for i in range(len([char for char in s]) - 1):
        if s[i] == s[i + 1]:
            counter += 1

    return counter


print(alternatingCharacters("AAAA"))
"""
3
"""

print(alternatingCharacters("BBBBB"))
"""
4
"""

print(alternatingCharacters("ABABABAB"))
"""
0
"""

print(alternatingCharacters("BABABA"))
"""
0
"""

print(alternatingCharacters("AAABBB"))
"""
4
"""
