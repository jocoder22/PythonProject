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

# formatting with Type
# string(position:conversion)
ex1 = [i for i in range(25)]
myex_list = list()
myex_list2 = list()
for i in ex1:
    if i < 4:
        print('This is 2 decimal places {:.2f}'.format(i))
        myex_list.append(float(i))
print(myex_list)
for n in myex_list:
    result = n ** 4
    myex_list2.append(result)
    print('This is integer: {:.0f}'.format(result))

binary_dict = dict()
octal_dict = dict()
hex_low_dict = dict()
hex_up_dict = dict()
exponent_dict = dict()
for n in ex1:
    result = n ** 4
    binary_dict[result] = '{:b}'.format(result) 
    octal_dict[result] = '{:o}'.format(result) 
    hex_low_dict[result] = '{:x}'.format(result) 
    hex_up_dict[result] = '{:X}'.format(result) 
    exponent_dict[result] = '{:e}'.format(result) 
    # print('This is binary: {:b}'.format(result))
    # print('This is octal: {:o}'.format(result))
    # print('This is hexadecimal with lowercase letters after 9: {:x}'.format(result))
    # print('This is hexadecimal with upperrcase letters after 9: {:X}'.format(result))
    # print('This is exponent notation: {:e}'.format(result))

print(myex_list2)
print(binary_dict)
print(octal_dict)
print(hex_low_dict)
print(hex_up_dict)
print(exponent_dict)

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
    print(mylist)
    print(len(mylist))
    return mylist

def wordPermut(w):
    from itertools import permutations
    mylist2 = list()
    permutSet = permutations(w)

    for i in list(permutSet):
        mylist2.append(''.join(i))
    print(mylist2)
    print(len(mylist2))
    return mylist2


# shuffle_word("tlcccr")
# myword = "tlcccr"
# wordPermut("tlcccr")
# word_form("dkeke", "loos")
# shuffle_word("tlcccr")

# ti = timeit.timeit('wordPermut(myword)', number=10, globals=globals())
# t2 = timeit.timeit('shuffle_word(myword)', number=10, globals=globals())

def program_performance(a, b, c):
    import timeit
    f1 = a.__name__
    f2 = b.__name__
    t11 = timeit.timeit('a(c)', number=100, globals=locals())
    t22 = timeit.timeit('b(c)', number=100, globals=locals())
    if t11 > t22: 
        r = round(t11/t22, 1)
        print('{} is {} times faster then {}'.format(f2, r, f1))
    else: 
        r = round(t22/t11, 1)
        print('{} is {} times faster then {}'.format(f1, r, f2))

# program_performance(shuffle_word , wordPermut, "boutte")