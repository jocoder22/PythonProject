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