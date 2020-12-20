def hourglassSum(arr):
    row = len(arr[0]) - 2
    col = len(arr) - 2
    largest_sum = -63

    for i in range(col):
        for j in range(row):
            top = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            mid = arr[i + 1][j + 1]
            bot = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            hgSum = top + mid + bot

            if largest_sum < hgSum:
                largest_sum = hgSum

    return largest_sum


arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

print(hourglassSum(arr))
