def maximumToys(prices, k):
    sumPrice, counter = 0, 0
    prices = sorted(prices)
    print(prices)

    for i in prices:
        sumPrice += i
        counter += 1
        if sumPrice > k:
            sumPrice -= i
            counter -= 1
            return counter

    return counter


print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))
