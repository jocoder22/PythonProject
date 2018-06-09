#!/usr/bin/env python
import re

# named group

p = r'(?P<group1>\bE\w+)+\W(?P<group2>\w+)'
pattern = re.compile(p, re.I)
text = "The school baseball team is in the  Eve evening loop"
result = pattern.search(text) 
result.group(1)  # 'Eve'
result.group('group1') # 'Eve' 
result.groupdict()  # {'group1': 'Eve', 'group2': 'evening'}


# backreference and conditional
zipcode = r'((?P<code1>\d{5})-(?(code1)(\d{2})|(\w{2})))'
correctzip = re.search(zipcode, '12222-6879')


extension = r'((?P<area>\d{3})-(?P=area)-\d{4} (?P<ex>Ext-)(?(ex)\d{4}))'
check = re.compile(extension)
correctext = check.search('121-456-873 Ext-5698')



