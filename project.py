#!/usr/bin/env python
import doctest, random, timeit, re
from functools import reduce
# import pdb; pdb.set_trace()

class Memiozation:
	def __init__(self, fn):
		self.fn = fn
		self.memorize = {}

	def __call__(self, arg):
		if arg not in self.memorize:
			self.memorize[arg] = self.fn(arg)
			return self.memorize[arg]


# reverse
xlist = [5,6,7, "man", 8, 9,"girl"]
xtuple = (7,4,"gon","dog")
x = "Woman"

def reverse1(parameter):
    return parameter[::-1]

# for list
def reverse2(parameter_list):
	'''
	This function reverses a given list

	Input: List
	Output: List

	Test:
	>>> reverse2([3, 6, 7, 1, 2, 5])
	[5, 2, 1, 7, 6, 3]
	>>> reverse2(['man', 8, 'open', 'bed', 5])
	[5, 'bed', 'open', 8, 'man']
	>>> reverse2(['good', 'lean', 'luke', 'shiny'])
	['shiny', 'luke', 'lean', 'good']
	'''
	parameter_list.reverse()
	return parameter_list

    
print(reverse2([3, 6, 7, 1, 2, 5]))
data = xlist
xl_reversed =  list(data[i] for i in range(len(data)-1, -1, -1))
data = xtuple
xt_reversed = tuple(data[i] for i in range(len(data)-1, -1, -1))
data = x
x_reversed = "".join(data[i] for i in range(len(data)-1, -1, -1))

print(xl_reversed)
print(xt_reversed)
print(x_reversed)

# reverse for list
def revelist(for_list):
	'''
	This function reverses a given list

	Input: List
	Output: List

	Test:
	>>> revelist([3, 6, 7, 1, 2, 5])
	[5, 2, 1, 7, 6, 3]
	>>> revelist(['man', 8, 'open', 'bed', 5])
	[5, 'bed', 'open', 8, 'man']
	>>> revelist(['good', 'lean', 'luke', 'shiny'])
	['shiny', 'luke', 'lean', 'good']
	'''
	newlist = []
	for i in range(len(for_list)-1,-1,-1):
		newlist.append(for_list[i])
	return newlist

# reverse for tuple
def revetup(for_tuple):
	newtuple = ()
	for i in range(len(for_tuple)-1,-1,-1):
		newtuple += (for_tuple[i],)
	return newtuple

# reverse for string
def revest(for_string):
	newstring = ''
	for i in range(len(for_string)-1,-1,-1):
		newstring += (for_string[i])
	return newstring


# reverse recursive
def rev_recur(s):
	'''
	This function reverses a given string

	Input: string
	Output: string

	Test:
	>>> rev_recur('kdkdmfjdiad')
	'daidjfmdkdk'
	>>> rev_recur('nam5')
	'5man'
	>>> rev_recur('goodluke')
	'ekuldoog'

	'''
	if len(s) <= 1 :
		return s

	return rev_recur(s[1:]) + s[0]




# Implement Balanced check

def balance_check(s):
	'''
	This function check for balanced parentheses in a string s, the string
	contains only parentheses without spaces or other strings or numbers


	Input: strings
	output: Boolean

	Test:
	>>> balance_check('[]')
	True
	>>> balance_check('(){}{{{}}}[][[]]')
	True
	>>> balance_check('((()))[][][][{{}])')
	False
	'''
	if len(s) % 2 != 0:
		return False

	openings = set('{[(')
	matches = set([('(',')'), ('{','}'), ('[',']')])
	
	stack = []

	for item in s:
		if item in  openings:
			stack.append(item)

		else:
			if len(stack) == 0:
				return False
			
			last_opening = stack.pop()

			if (last_opening, item) not in matches:
				return False


	return len(stack) == 0



# Permutation using recursion
def permute(s):
	'''
	This function return permutation of a given string

	Input: string

	Output: List

	Test:
	>>> permute('mNgO')
	['mNgO', 'mNOg', 'mgNO', 'mgON', 'mONg', 'mOgN', 'NmgO', 'NmOg', 'NgmO', 'NgOm', 'NOmg', 'NOgm', 'gmNO', 'gmON', 'gNmO', 'gNOm', 'gOmN', 'gONm', 'OmNg', 'OmgN', 'ONmg', 'ONgm', 'OgmN', 'OgNm']
	>>> permute('345') 
	['345', '354', '435', '453', '534', '543']
	>>> permute('ABC')
	['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
	'''

	output = []
	# base case
	if len(s) == 1:
		output = [s]
	
	else:
		for i, letter in enumerate(s):
			for p in permute(s[:i] + s[i+1:]):
				# print(f'Before addition the letter was : {letter}')
				# print(f'Before addition letter to permute was : {p}')
				# print(f'Before addition  output was : {output}')
				output += [letter + p]
				# print(f'After addition  output is now : {output}')
	
	return output


# Fibonnaci Sequence
def fibo_iter(n):
	'''
	This function returns the sum of Fibonnaci Sequence
	 
	Input: Interger
	 
	Output: Interger
	 
	Test:
	>>> fibo_iter(10)
	55
	>>> fibo_iter(100)
	354224848179261915075
	>>> fibo_iter(0)
	0
	'''
	a, b = 0, 1

	for i in range(n):
		a, b = b, a+b
	
	return a



@Memiozation
def fibo_iter1(n):
	a, b = 1, 1

	for i in range(n -1):
		a, b = b, a+b
	return a


def fibo_rec(n):
	# Base case
	if n == 0 or n == 1:
		return n
	else:
		return fibo_rec(n-1) + fibo_rec(n-2)
	

# Using cache for memiozation
def fibo_d(n):
	cache = [None] * (n+1)
	# Base case using recursive method
	if n == 0 or n == 1:
		return n

	# check cache
	if cache[n] != None:
		return cache[n]

	# keep setting Cache
	cache[n] = fibo_d(n-1) + fibo_d(n -2)

	return cache[n]



def gen_fibon(n):

	a = 1
	b = 1

	for i in range(n):
		yield a
		a, b =  b, a+b

for number in gen_fibon(10):
	print(number)



def rand_num(low, high, n):
	for i in range(n):
		yield random.randint(low, high)

for num in rand_num(2, 12, 7):
	print(num)

# Coin change problem
def coinchange(target, coins_list):
	# Default number of coins set to target
	# Based on assumption that the least coin denomination to be 1 unit
	min_coins = target

	# check if the target amount is in the list already
	if target in coins_list:
		return 1

	else:
		# For every coin value that is less than the target
		for i in [c for c in coins_list if c <= target]:
			# num_coins is the counter here
			# Add 1 to counter per each recurssion
			# substract the coin value from the target
			num_coins = 1 + coinchange(target-i, coins_list)

			if num_coins < min_coins:
				min_coins = num_coins

	return min_coins




# Coin change problem 2
# Using Memiozation
# This is time efficient but memory expensive
def coinchange_M(target, coins_list, cache):
	# Default number of coins set to target
	# Based on assumption that the least coin denomination to be 1 unit
	# cache = [0] * (target + 1)
	min_coins = target

	# check if the target amount is in the list already
	if target in coins_list:
		cache[target] = 1
		return 1
	
	elif cache[target] > 0:
		return cache[target]

	else:
		# For every coin value that is less than the target
		for i in [c for c in coins_list if c <= target]:
			# num_coins is the counter here
			# Add 1 to counter per each recurssion
			# substract the coin value from the target
			num_coins = 1 + coinchange_M(target-i, coins_list, cache)

			if num_coins < min_coins:
				min_coins = num_coins
				cache[target] = min_coins

	return min_coins




def prod(n):
	'''
	This function returns the product of positive number up to n
	 
	Input: Integer
	 
	Output: Interger
	 
	Test:
	>>> prod(-2)
	The number must be a postive Integer
	>>> prod(0)
	0
	>>> prod(1) 
	1
	>>> prod(5) 
	120
	'''
	if n < 0:
		print('The number must be a postive Integer')
	elif n <= 1:
		return n
	else:
		return n * prod(n - 1)





def prod2(N):
	'''
	>>> prod2(5)
	120
	'''
	if N <= 1:
		return N
	else:
		result = 1
		for i in range(1, N + 1):
			result *= i
	return result


# product using reduce

def prod3(N):
	lst = list(range(1, N+1))
	return reduce(lambda x,y: x*y, lst)

cache2 = [0] * (74 + 1)
print(fibo_d(10))
print(coinchange(15,[1,5,10]))
print(coinchange_M(74,[1,5,10,25], cache2))



# using timeit
# print(timeit.timeit("prod(30)", globals=globals()))
# print(timeit.timeit("prod2(30)", globals=globals()))
# print(timeit.timeit("prod3(30)", globals=globals()))
# print(timeit.timeit('"-".join(str(n) for n in range(101))', number=10000))
# print(timeit.timeit('"-".join(map(str,range(101)))', number=10000))





# Python debugger
t = [5, 6, 9, 4]
u = [4, 8]
# pdb.set_trace()
# print(t * u)





# Regular Expression
def mult_find(patterns, text):
	'''
	This function
	 
	Input:
	 
	Output:
	 
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











if __name__ == '__main__':
	doctest.testmod(verbose=True)
	# import timeit
	# print(timeit.timeit("prod(30)", setup="from __main__ import prod"))
	# doctest.testmod()



