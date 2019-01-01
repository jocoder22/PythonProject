#!/usr/bin/env python

import timeit

def program_performance(a, b, *c, d=1):
    import timeit
    f1 = a.__name__
    f2 = b.__name__
    if c:
        t11 = timeit.timeit('a(c)', number=d, globals=locals())
        t22 = timeit.timeit('b(c)', number=d, globals=locals())
    else:
        t11 = timeit.timeit('a()', number=d, globals=locals())
        t22 = timeit.timeit('b()', number=d, globals=locals())


    if t11 > t22: 
        r = round(t11/t22, 1)
        print('{} is {} times faster then {}'.format(f2, r, f1))
    else: 
        r = round(t22/t11, 1)
        print('{} is {} times faster then {}'.format(f1, r, f2))

