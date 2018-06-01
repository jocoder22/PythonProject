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





