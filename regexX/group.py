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
zipcode = r'((?P<code1>\d{5})(?(code1)(-\d{2})|(-\w{2})))'
correctzip = re.search(zipcode, '12222-6879')


extension = r'((?P<area>\d{3})-(?P=area)-\d{4}(?P<ex> Ext-)?(?(ex)(?=\d{4}$)|(?= \w{2}$)))'
check = re.compile(extension)
check2 = re.compile(
    r'''
    ((?P<area>\d{3})-(?P=area)-\d{4}
    (?P<ex> Ext-)?
    (?(ex)(?=\d{4}$)|(?= \w{2}$)))
    ''')


check3= re.compile(
    r'''
    ((?P<area>\d{3})-(?P=area)-\d{4}
    # Telephone number with extension
     (?P<ex> Ext-)? # extension is optional
    # Conndition expression based on extension
     (?(ex)(?=\d{4}$)|(?= \w{2}$))
    )
    ''',
    re.VERBOSE)


check4 = re.compile(
    r'''
    (?P<area>\d{3})-(?P=area)-\d{4}
    # Telephone is combination of area-code of same 3 digits separated by dash
    # this is followed by dash and 4 digits

    (?P<ex> Ext-)?
    # the extension i.e space followed by Ext- is optional

    # conditional expression:
    # if the extension is given:
    # the remainder must end in 4 digits  or
    # space and 2 alphanumeric letters
    (?(ex)(?=\d{4}$)|(?= \w{2}$))
    ''',
    re.UNICODE | re.VERBOSE)

correctext = check.search('121-456-873 Ext-5698') # None
check.match('123-123-2345 Ext-5645').groups() # ('123-123-2345 Ext-', '123', ' Ext-')
check.match('123-123-2345 NY').groups() # ('123-123-2345', '123', None)


