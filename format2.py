#!/usr/bin/env python

for i in range(40):
    print(i, end='')
    
print()

# formating using keyword argument
print('This is {x} {} in {}'.format('morning', 'USA', x='Christmas'))
print('This is {x} {1} in {0}'.format('morning', 'USA', x='Christmas'))