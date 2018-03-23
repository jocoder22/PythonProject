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
test_patterns3 = [ r'\d+',  	# sequence of digits
				  r'\D+',		# sequence of non digits
				  r'\s+',		# sequence of whitespaces
				  r'\S+',		# sequence of non whitespaces
				  r'\w+',		# alphanumeric characters
				  r'\W+',		# non-alphanumeric characters
				]

mult_find(test_patterns,test_text)
mult_find(test_patterns2,test_text2)
mult_find(test_patterns3,test_text3)

# Exclusing by ^ e.g [^...]
text_exclusion = 'Hello! Thanks. What is this?. I am fine.'
pattern_exclusion = '[^!.? ]+'

print(re.findall(pattern_exclusion,text_exclusion))


def regxx(expr, s):
	ss = s.split()
	if re.search(expr, s):
		print(f'Some {expr} found in {s} :-)')
		print(re.search(expr,s))
	else:
		print(f'No {expr} found :-)')

### Any Character .
expr1 = r' .at '
s = 'cat and rat are have high rating at music education and communication'



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)