#!/usr/bin/env python

import re

# split(string, maxsplit=0) --> returns a list


text = 'This is a bright sunny day'
pattern = r'\W'
result = re.compile(pattern)
split_result = result.split(text)

# find number of element in the list
len(split_result)

# maxsplit -- maximum number of split you want
# if less than maximum possible splits, returns the remainder
# if maxsplit > maximum possible splits, returns all possible splits
result_maxsplit = result.split(text, 3)

pat = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# word count
word_list = result.split(pat)
len(word_list)

# return match pattern also by using grouping
# the use of group will add the pattern to the result
yy = re.compile(r'and')
yyy = re.compile(r'(and)')

tex = 'Bright and Heaver and Food and Good'
yy.split(tex)
# ['Bright ', ' Heaver ', ' Food ', ' Good']

yyy.split(tex)
# ['Bright ', 'and', ' Heaver ', 'and', ' Food ', 'and', ' Good']