#!/usr/bin/env python
import doctest
'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''


def permute(s):
    '''
    This function returns the permutation of a given string
     
    Input: string
    Output: string
     
    Test: 
    >>> permute('AFG')
    ['AFG', 'AGF', 'FAG', 'FGA', 'GAF', 'GFA']
    >>> permute('123')
    ['123', '132', '213', '231', '312', '321']
    >>> permute('E T')
    ['E T', 'ET ', ' ET', ' TE', 'TE ', 'T E']
    '''
    out = []
    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i + 1:]):
                out += [let+perm]
    
    return out







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




# using timeit
print(timeit.timeit("prod(30)", globals=globals()))
print(timeit.timeit("prod2(30)", globals=globals()))
print(timeit.timeit("prod3(30)", globals=globals()))



if __name__ == '__main__':
    doctest.testmod(verbose=True)
