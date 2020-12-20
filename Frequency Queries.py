from collections import defaultdict


def freqQuery(queries):
    database = defaultdict(int)
    frequences = defaultdict(int)

    output = list()

    for q in queries:
        op, val = q

        if op == 1:
            frequences[database[val]] = max(0, frequences[database[val]] - 1)
            database[val] += 1
            frequences[database[val]] += 1
        elif op == 2:
            frequences[database[val]] = max(0, frequences[database[val]] - 1)
            database[val] = max(0, database[val] - 1)
            frequences[database[val]] += 1
        elif op == 3:
            if frequences[val] > 0:
                print("1")
                output.append(1)
            else:
                print("0")
                output.append(0)

    return output


"""
1x -> Insert x in your data structure
2y -> Delete one occurence of y from your data structure, if present
3z -> Check if any integer is present whose frequency is exactly
      If yes, print 1 else 0
"""

print(freqQuery([(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]))
"""
0
1
[0, 1]
"""

print(freqQuery([(3, 4), (2, 1003), (1, 16), (3, 1)]))
"""
0
1
[0, 1]
"""

print(freqQuery([(1, 3), (2, 3), (3, 2), (1, 4), (1, 5), (1, 5), (1, 4), (3, 2), (2, 4), (3, 2)]))
"""
0
1
1
[0, 1, 1]
"""

print(freqQuery([(1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2)]))
"""
0
1
[0, 1]
"""
