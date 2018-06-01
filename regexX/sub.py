#!/usr/bin/env python

import re

# sub(repl, string, count=0) --> with compilation
# sub(pattern, repl, string, count=0) --> without compilation
# re.sub returns the modified string

text = 'Mary birthday is on 20th of May'
pattern = r'[0-9]+'
replace = re.compile(pattern)

newBirthday = replace.sub("23",text)
print(newBirthday)

# re.sub will replace the leftmost non-overlapping match
text2 = "My telephone number is 222-222-2222"
phonePattern = r'22'
newNumber = re.sub(phonePattern, "55", text2)
print(newNumber)
