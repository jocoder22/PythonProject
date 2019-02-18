#!/usr/bin/env python
import re, doctest, timeit


# Regular Expression
def mult_find(patterns, text):
	'''
	This function finds patterns in a given string

	Input: String
	 
	Output: List
	 
	Test:
	>>> 
	 
	>>> 
	 
	>>> 
	 
	'''
	for pattern in patterns:
		print(f'Searching for {pattern} in {text}')
		print(re.findall(pattern, text))
		print('\n')


test_text = 'sdsd..sssddd...sdddsddd...dsds...dsssss..sdddd..sssdd..ssdsssd'
test_text2 = 'This is an example. Let see if there are A b C D e in letters'
test_patterns = [ 'sd*',  		# s followed by zero or more d's
				  'sd+',		# s followed by one or more d's
				  'sd?',		# s followed by zero or one d's
				  'sd{3}',		# s followed by three d's
				  'sd{2,3}',	# s followed by two or three d's
				  's+d',		# one or more s's followed by d
				  '[sd]',		# either s or d
				  's[sd]+', 	# s followed by one or more of either s or d
				]


test_patterns2 = [ '[a-z]',  		# lower case a to z
				  '[A-Z]',			# Upper case A to Z
				  '[a-zA-Z]',		# lower case a to z or upper case A to Z
				  '[A-Z][a-z]+',	# Upper case A to Z and one or more lower case a to z
				]


test_text3 = 'This is a string with Numbers 1238, symbols #$hast, 234-real'
test_patterns3 = [r'\d+',  	    # sequence of digits, this is equivalent to the class [0-9].
				  r'\D+',		# sequence of non digits, this is equivalent to the class [^0-9].
				  r'\s+',		# sequence of whitespaces, this is equivalent to the class [ \t\n\r\f\v].
				  r'\S+',		# sequence of non whitespaces, this is equivalent to the class [^ \t\n\r\f\v].
				  r'\w+',		# alphanumeric characters,  this is equivalent to the class [a-zA-Z0-9_]
				  r'\W+',		# non-alphanumeric characters,  this is equivalent to the class [^a-zA-Z0-9_]
				]

mult_find(test_patterns, test_text)
mult_find(test_patterns2, test_text2)
mult_find(test_patterns3, test_text3)

# Exclusing by ^ e.g [^...]
text_exclusion = 'Hello! Thanks. What is this?. I am fine.'
pattern_exclusion = '[^!.? ]+'

print(re.findall(pattern_exclusion, text_exclusion))


def regxx(expr, s):
	'''
    This function use regular expressions.

    Input: String
    Output: List

    Test:
    >>> ss = 'The cats are in the room with rat and cattle'
    >>> regxx(r'cat', ss)
    ['cat', 'cat']
    >>> regxx(r'cat.', ss)
    ['cats', 'catt']
    >>> regxx(r'\b.at.\b',ss)
	['cats', 'rat ']
	'''
	if re.search(expr, s):
		print(re.findall(expr, s))
	else:
		print(f'No match found  in {s} :-)')

### Any Character .
expr1 = r'.at'
expr2 = r'cat?'
expr3 = r' cat '
s = 'cat and rat are have high rat thing at music education and communication'
s2 = 'There are many cats in the cattle catch roacat'
s3 = 'In the end cat and rat are catching fire'



## using logical 'OR' operator, |
mm = 'January February March April May June July August September October November December'
mbermonth = re.findall(r"\w*mber|\w*uary",mm)



# Greedy and non-greedy re
# Greedy search
tag = '<div><em>This is a wonderful day</em><div>'
tagfind = re.search(r'<.*>', tag)
print(tagfind.group()) # <div><em>This is a wonderful day</em><div>


# Non-greedy search
NonGreedy = re.search(r'<.*?>', tag)
print(NonGreedy.group()) # <div>





if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)