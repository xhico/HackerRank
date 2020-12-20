def rotLeft(a, d):
    n = len(a)
    return [a[(d % n + i) % n] for i in range(n)]


a = [1, 2, 3, 4, 5]
d = 4
print(rotLeft(a, d))
