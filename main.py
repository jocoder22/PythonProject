#!/usr/bin/env python

# reverse
xlist = [5,6,7, "man", 8, 9,"girl"]
xtuple = (7,4,"gon","dog")
x = "Woman"

def reverse1(parameter):
    return parameter[::-1]

# for list
def reverse2(parameter_list):
    return parameter.reverse()

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



# Implement Balanced check

def balance_check(s):
	'''
	This is the docstring
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

balance_check('[]')
balance_check('(){}{{{}}}[][[]]')
balance_check('((()))[][][][{{}])')