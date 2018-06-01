#!/usr/bin/env python

import re

# split(string, maxsplit=0)

text = 'This is bright sunny day'
pattern = r'\W'
result = re.compile(pattern)
split_result = result.split(text)



