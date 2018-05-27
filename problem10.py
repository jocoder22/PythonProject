#!/usr/bin/env python


def sumUP(lst, target):
    seen = set()

    for i in lst:
        num2 = target - i

        if num2 in seen:
            return True

        seen.add(i)
    
    return False


def sumUP2(lst, target):
    
    for i in lst:
        if target >= i:
            num2 = target - i

            if num2 in lst:
                return True
    
    return False

sumUP([5,6,7,4,7,2],16)
sumUP([5,6,7,4,7,2],11)
sumUP2([5,6,7,4,17,2],19)
sumUP2([15,6,7,4,7,2],10)