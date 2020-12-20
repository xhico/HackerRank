from collections import Counter


def twoStrings(s1, s2):
    s1, s2 = Counter(s1), Counter(s2)
    return 'NO' if s1 - s2 == s1 else 'YES'


print(twoStrings("hello", "word"))
print(twoStrings("hi", "word"))
print(twoStrings("wouldyoulikefries", "abcabcabcabcabcabc"))
print(twoStrings("hackerrankcommunity", "cdecdecdecde"))
print(twoStrings("jackandjill", "wentupthehill"))
print(twoStrings("writetoyourparents", "fghmqzldbc"))

"""
YES
NO
NO
YES
YES
NO
"""
