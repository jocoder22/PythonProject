#!/usr/bin/env python


def coinMaker(n, coins):
    arr = [1] + [0] * n

    for coin in coins:
        for i in range(coin, n+1):
            arr[i] += arr[i - coin]

    if n == 0:
        return 0
    else:
        return arr[n]


coinMaker(100, [1, 3, 6])
coinMaker(200, [10, 5, 20])
