#!/usr/bin/env python
import re

# named group

p = r'(?P<group1>\bE\w+)+\W(?P<group2>\w+)'
pattern = re.compile(p, re.I)
text = "The school baseball team is in the  Eve evening loop"
result = pattern.search(text) # ['Eve', 'evening']


