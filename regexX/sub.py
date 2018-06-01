#!/usr/bin/env python

import re

# sub(repl, string, count=0) --> with compilation
# sub(pattern, repl, string, count=0) --> without compilation

text = 'Mary birthday is on 20th of May'
pattern = r'[0-9]+'
replace = re.compile(pattern)

newBirthday = replace.sub("23",text)
print(newBirthday)
