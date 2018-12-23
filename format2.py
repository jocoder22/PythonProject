#!/usr/bin/env python

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
    for _ in range(5000):
        st = [i for i in s]
       
        random.shuffle(st)
        new = "".join(st)

        if new not in mylist:
            mylist.append(new)
    print(mylist)
    print(len(mylist))
    return mylist

def wordPermut(w):
    from itertools import permutations
    mylist2 = list()
    permutSet = permutations(w)

    for i in list(permutSet):
        if i not in mylist2:
            mylist2.append(''.join(i))
    print(mylist2)
    print(len(mylist2))


shuffle_word("tlcccr")

word_form("dkeke", "loos")
