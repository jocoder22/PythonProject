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

word_form("dkeke", "loos")
