#!/usr/bin/env python

import re

# sub(repl, string, count=0) --> with compilation
# sub(pattern, repl, string, count=0) --> without compilation
# re.sub returns the modified string

text = 'Mary birthday is on 20th of May'
pattern = r'[0-9]+'
replace = re.compile(pattern)

newBirthday = replace.sub("23",text)
print(newBirthday) # Mary birthday is on 23th of May


# re.sub will replace the leftmost non-overlapping match
text2 = "My telephone number is 222-222-2222"
phonePattern = r'22'
newNumber = re.sub(phonePattern, "55", text2)
print(newNumber) # My telephone number is 552-552-5555


# repl can be a function
# in the example our pattern is a group
def repl_function(matchobj):
    if matchobj.group(1) in r'[0,1,2,3,4]':
        return '9'
    else:
        return 's'

text2a = 'A good day 32'
newAddress =  re.sub('([a-zA-Z0-9])', repl_function, text2a)
print(newAddress) # s ssss sss 99 


def repl_function2(matchobj):
    if matchobj.group(1) == 'Boy': return "John"
    else: return matchobj(1)

print(re.sub(r'(Boy)', repl_function2, 'Boy is a man')) # John is a man

# using lambda
text2b = 'In the 2nd of june, on the 2nd day and in the 3rd year'
labf = re.compile(r'\d+')
labrep = labf.sub(lambda a: a.group(0)+'3', text2b)
# 'In the 23nd of june, on the 23nd day and in the 33rd year'

# using dictionary
items = {"coffe":3, "sugar":8, "milk":1, "donut":5, "bread":6}

def itemR(a):

    item = a.group(0)

    if item in items:
        return "XX"
    else: return item

ppitem = re.compile(r'\w+')
pptext = 'I need coffe, tea, rice, donut, beans and bread'
ppitem.sub(itemR, pptext) # 'I need XX, tea, rice, XX, beans and XX'



# using subn
# subn(repl, string, count=0) --> with compilation
# subn(pattern, repl, string, count=0) --> without compilation
# re.subn returns a tuple with substituted string and number of substitutions made
textn = "This is the 15th of March, 1990 records"
subnPattern = re.compile(r'(\d+[\w+]?)|^T|s$')
subnn = subnPattern.subn('xx', textn)
print("Final result: ", subnn[0])
print("Substitutions made: ", subnn[1])

subb = re.compile(r'(?i)\b[tm]+\w*\b')
subb2 = subb.subn('XX', textn)
print("Final result: ", subb2[0])
print("Substitutions made: ", subb2[1])

textn2 = textn + " not march but June"
sub2 = subb.subn("XX", textn2)
print("Final result: ", sub2[0])
print("Substitutions made: ", sub2[1])




