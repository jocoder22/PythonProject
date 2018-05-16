#!/usr/bin/env python


# Using looping technique
def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


# Using recursion
def fibR(n):
    if n == 1 or n == 2:
        return 1
    return fibR(n-1) + fibR(n-2)


a, b = 0, 1


# Using generators
def fibI():
    global a, b
    while True:
        a, b = b, a+b
        yield a


# Using memoization
def fibmemo(fn, arg):
    memo = {}
    if arg not in memo:
        memo[arg] = fn(arg)
    return memo[arg]


fibm = fibmemo(fib, 7)
print(fibm)


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

