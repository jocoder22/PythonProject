#!/usr/bin/env python


def squareRoot(n):
    if n < 0:
        return ValueError

    if n == 1:
        return 1

    for k in range((n / 2) + 1):
        if k**2 == n:
            return k

        elif k**2 > n:
            return k - 1

    return k

