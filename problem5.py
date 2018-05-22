#!/usr/bin/env python


def squareRoot(n):
    if n < 0:
        return ValueError

    if n == 1:
        return 1

    for k in range((n // 2) + 1):
        if k**2 == n:
            return k

        elif k**2 > n:
            return k - 1

    return k


def better_square(n):
    if n < 0:
        return ValueError

    if n == 1:
        return 1

    low = 0
    high = (n // 2) + 1

    while low + 1 < high:
        mid = low + (high - low)//2

        square = mid ** 2

        if square == n:
            return mid
        elif square < n:
            low = mid
        else:
            high = mid
    return low


squareRoot(89)
better_square(56)

squareRoot(124)
better_square(371)


