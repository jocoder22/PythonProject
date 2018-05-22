#!/usr/bin/env python


def threeM(lst):
    high = max(lst[0], lst[1])
    low = min(lst[0], lst[1])

    high_prod2 = lst[0]*lst[1]
    low_prod2 = lst[0]*lst[0]

    high_prod3 = lst[0]*lst[1]*lst[2]

    for num in lst[2:]:
        high_prod3 = max(high_prod3, num*high_prod2, num*low_prod2)

        high_prod2 = max(high_prod2, num*high, num*low)
        low_prod2 = max(low_prod2, num*high, num*low)

        high = max(high, num)
        low = min(low, num)

    return high_prod3


threeM([90, 10, 59, 87, -15, -33, 36, 91, 12, 53])
threeM([19, 20, 7, 18, -17, -39, 6, 21, 12, 23, 11, 30, 14, 22, -25, -42])
