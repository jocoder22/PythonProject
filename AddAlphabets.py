#!/usr/bin/env python

import time
import timeit
import string
from program_timer import program_performance


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

# print(numsum(good))
# print(numsum2(good))
# timefunc = timeitout(numsum, good)
# print(timeit.timeit(timefunc, number=100000))
# print(timeit.timeit("numsum(good)", number=100000, globals=globals()))
# print(timeit.timeit("numsum2(good)", number=100000, globals=globals()))


program_performance(numsum, numsum2, "FLKDFDKLrukadd")

def numsum3(str):
	a_ = list(string.ascii_lowercase)
	total = 0
	for ab_ in str:
		for index, value in enumerate(a_):
			if ab_.lower() == value:
				total += index + 1
	
	return total

# print(numsum3(good))
# print(timeit.timeit("numsum3(good)", number=100000, globals=globals()))

# program_performance(numsum3, numsum2, "FLKDFDKLrukadd")

def time_func(funt):
	n_ = 100000
	time0 = time.time()
	for _ in range(n_): funt
	time1 = time.time()

	totalTime = time1-time0
	return totalTime

time_func(numsum("PIDAHDKDkahudjhlad"))



