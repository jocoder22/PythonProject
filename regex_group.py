#!/usr/bin/env python

import re


text = 'Babamiloo'
pattern = r'(ba)'
mysearch = re.compile(pattern)
print(mysearch.match(text))
