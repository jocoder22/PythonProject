#!/usr/bin/env python

import time
import timeit
import string

def numsum(str):
	a_ = list(string.ascii_lowercase)
	n_ = list(range(1,27))
	d_ = dict(zip(a_, n_))
	total = 0
	for ab_ in str:
		for key, value in d_.items():
			if ab_.lower() == key:
				total +=  value

	return total
		
	
def numsum2(str):
	a_ = list(string.ascii_lowercase)
	total = 0
	for ab_ in str:
		value = a_.index(ab_.lower()) + 1
		total +=  value
	
	return total


def timeitout(func, *args, **kwargs):
	def wrapper():
		return func(*args, **kwargs)
	return wrapper
	

good = "FLKDFDKLrukadd"

timefunc = timeitout(numsum, good)
timeit.timeit(timefunc, number=10000)
timeit.timeit("numsum(good)", number=10000, globals=globals())

