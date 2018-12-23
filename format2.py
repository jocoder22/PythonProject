#!/usr/bin/env python

import timeit

for i in range(40):
    print(i, end='')
    
print()

# formating using keyword argument
print('This is {x} {} in {}'.format('morning', 'USA', x='Christmas'))
print('This is {x} {1} in {0}'.format('morning', 'USA', x='Christmas'))

# Type formatting
s1 = 'This is {} {}'.format('String', 'One')
print(s1)
print([i for i in range(10)])

def word_form(*args):
    for k in args:
        for i in k:
           print(i, end='   ')
        print('')


def shuffle_word(s):
    import random
    mylist = list()
    st = [i for i in s]
    for _ in range(1000):
       
        random.shuffle(st)
        new = "".join(st)

        if new not in mylist:
            mylist.append(new)
    # print(mylist)
    # print(len(mylist))
    return mylist

def wordPermut(w):
    from itertools import permutations
    mylist2 = list()
    permutSet = permutations(w)

    for i in list(permutSet):
        mylist2.append(''.join(i))
    # print(mylist2)
    # print(len(mylist2))
    return mylist2


# shuffle_word("tlcccr")
myword = "tlcccr"
wordPermut("tlcccr")
word_form("dkeke", "loos")
shuffle_word("tlcccr")

ti = timeit.timeit('wordPermut(myword)', number=10, globals=globals())
t2 = timeit.timeit('shuffle_word(myword)', number=10, globals=globals())

def program_performance(a , b , c):
    import timeit
    t11 = timeit.timeit('a(c)', number=100, globals=globals())
    t22 = timeit.timeit('b(c)', number=100, globals=globals())
    if t11 > t22: 
        r = round(t11/t22, 1)
        print('{} is {} times faster then {}'.format(a, r, b))
    else: 
        r = round(t22/t11, 1)
        print('{} is {} times faster then {}'.format(b, r, a))

