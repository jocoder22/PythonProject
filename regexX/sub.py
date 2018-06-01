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


# repl can be a function
# the pattern must be a group
def repl_function(matchobj):
    if matchobj.group(1) in r'[0,1,2,3,4]':
        return '9'
    else:
        return 's'

text2a = 'A good day 32'
newAddress =  re.sub('([a-zA-Z0-9])', repl_function, text2a)
print(newAddress)


def repl_function2(matchobj):
    if matchobj.group(1) == 'Boy': return "John"
    else: return matchobj(1)

print(re.sub(r'(Boy)', repl_function2, 'Boy is a man'))
