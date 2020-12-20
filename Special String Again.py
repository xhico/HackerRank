# Complete the substrCount function below.
def substrCount(n, s):
    class Repeater(object):
        def __init__(self, char, count):
            self.char = char
            self.count = count

    # 1st round, build repeaters
    curr, count = None, 0
    repeaters = []
    for i in s:
        if i == curr:
            count += 1
        else:
            if curr is not None:
                repeaters.append(Repeater(curr, count))
            curr, count = i, 1
    repeaters.append(Repeater(curr, count))  # append the last case

    # 2nd round, calculate one repeater one time
    answer = 0
    for repeater in repeaters:
        # the formula: 3 => 3*4//2 = 6, 4 => 4*5//2 = 10
        answer += (repeater.count * (repeater.count + 1)) // 2

    # 3rd round, caculate 3 repeaters joining together
    for i in range(2, len(repeaters)):
        first, second, third = repeaters[i - 2:i + 1]
        if second.count == 1 and first.char == third.char:  # palindrome only allows one diff letter in the middle.
            answer += min(first.count, third.count)

    return answer


print(substrCount(5, "asasd"))
print(substrCount(7, "abcbaba"))
print(substrCount(4, "aaaa"))
"""
7
10
10
"""
