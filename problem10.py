#!/usr/bin/env python


def sumUP(lst, target):
    seen = set()

    for i in lst:
        num2 = target - i

        if num2 in seen:
            return True

        seen.add(i)
    
    return False