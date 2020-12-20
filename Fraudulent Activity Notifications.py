from itertools import islice
from collections import deque
from bisect import insort, bisect_left


def activityNotifications(seq, M):
    seq = iter(seq)
    s = []
    m = M // 2

    # Set up list s (to be sorted) and load deque with first window of seq
    s = [item for item in islice(seq, M)]
    d = deque(s)

    # Simple lambda function to handle even/odd window sizes
    median = lambda: s[m] if bool(M & 1) else (s[m - 1] + s[m]) * 0.5

    # Sort it in increasing order and extract the median ("center" of the sorted window)
    s.sort()

    # Now slide the window by one point to the right for each new position (each pass through
    # the loop). Stop when the item in the right end of the deque contains the last item in seq
    count = 0
    for item in seq:
        count += item >= 2 * median()
        old = d.popleft()  # pop oldest from left
        d.append(item)  # push newest in from right
        del s[bisect_left(s, old)]  # locate insertion point and then remove old
        insort(s, item)  # insert newest such that new sort is not required

    return count


print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
"""
2
"""

print(activityNotifications([1, 2, 3, 4, 4], 4))
"""
0
"""

print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
"""
2
"""
