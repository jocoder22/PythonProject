#!/usr/bin/env python

import re


text = 'Babamiloo'
pattern = r'(ba)'
mysearch = re.compile(pattern)
print(mysearch.match(text))

text2 = 'My son in higher education lives with our cat catty'
pattern2 = r'(cat)\w+'
mysearch2 = re.compile(pattern2)
result = mysearch2.findall(text2)


# Looking for repeated word
pattern3 = r'\b(?P<repeat>\w+)\s+(?P=repeat)\b'
findrepeat = re.compile(pattern3)
text3 = 'In the morning morning of of june'
print(findrepeat.search(text3).group())

