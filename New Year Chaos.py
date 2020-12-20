def minimumBribes(q):
    bribes = 0

    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)


if __name__ == '__main__':
    n = 5
    q = [2, 1, 5, 3, 4]
    minimumBribes(q)

    q = [2, 5, 1, 3, 4]
    minimumBribes(q)
