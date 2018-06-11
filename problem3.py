#!/usr/bin/env python

import timeit


# Using looping technique
def fib(n):
    if n <= 0:
        print('Incorrect n: must be greater than zero')
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


def fib0(n):
    if n <= 0:
        print('Incorrect n: must be greater than zero')
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return a


def fibNet(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# Using recursion
def fibR(n):
    if n <= 0:
        print('Incorrect n: must be greater than zero')
    if n == 1 or n == 2:
        return 1
    return fibR(n-1) + fibR(n-2)


fib(22)
fib0(22)
fibR(22)
fibNet(22)

a, b = 0, 1


# Using generators
def fibI():
    global a, b
    while True:
        a, b = b, a+b
        yield a


g = fibI()
next(g)
next(g)


# Using memoization
def fibmemo(fn, arg):
    memo = {}
    if arg not in memo:
        memo[arg] = fn(arg)
    return memo[arg]


fibm = fibmemo(fib, 7)
fibm2 = fibmemo(fib, 45)
print(fibm, fibm2)


# Using memoization as decorator
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
            return self.memo[arg]


@Memoize
def fib2(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


print(fib2(5))
print(fib2(58))


# using timeit
print('Timed fib2:', timeit.timeit("fib2(30)", globals=globals()))
print('Timed fib:', timeit.timeit("fib(30)", globals=globals()))
print('Timed fib0:', timeit.timeit("fib0(30)", globals=globals()))
print('Timed fibmemo:', timeit.timeit("fibmemo(fib, 30)", globals=globals()))
print('Timed fib:', timeit.timeit("fib2(30)", globals=globals()))
