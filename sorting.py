
#!/usr/bin/env python
import doctest, timeit
from random import *

'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''

def bubble_sort(arr):
    '''
    This function performs bubble sort method
     
    Input: List
     
    Output: List
     
    Test:
    >>> arr = [5,3,8,4,5,90,23,14,2]
    >>> arr2 = [15,3,18,4,50,23,14,20]
    >>> bubble_sort(arr2)
    >>> bubble_sort(arr)
    >>> arr
    [2, 3, 4, 5, 5, 8, 14, 23, 90]
    >>> arr2
    [3, 4, 14, 15, 18, 20, 23, 50]
    '''

    # for every element arranged backward
    for n in range(len(arr)-1,0,-1):
        # the point to swtich
        for k in range(n):
            if arr[k] > arr[k +1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]

def bubble_sort2(arr):
    '''
    This function performs bubble sort method
     
    Input: List
     
    Output: List
     
    Test:
    >>> arr = [5,3,8,4,5,90,23,14,2]
    >>> arr2 = [15,3,18,4,50,23,14,20]
    >>> bubble_sort2(arr2)
    >>> bubble_sort2(arr)
    >>> arr
    [2, 3, 4, 5, 5, 8, 14, 23, 90]
    >>> arr2
    [3, 4, 14, 15, 18, 20, 23, 50]
    '''
    # for every element in the list
    for n in range(len(arr)):
        for k in range(0,len(arr)-n-1):
            if arr[k] > arr[k +1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]



setupme = "from random import shuffle"

thecode = '''
ku = shuffle([x for x in range(1000)])
def bubble_sort2(ku):
    # for every element in the list
    for n in range(len(arr)):
        for k in range(0,len(arr)-n-1):
            if arr[k] > arr[k +1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
'''

print(timeit.timeit(setup = setupme,
                    stmt = thecode,
                    number = 10000))



thecode = '''
ku = shuffle([x for x in range(1000)])
def bubble_sort(ku):
   for n in range(len(arr)-1,0,-1):
        # the point to swtich
        for k in range(n):
            if arr[k] > arr[k +1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]

'''

print(timeit.timeit(setup = setupme,
                    stmt = thecode,
                    number = 10000))


def Time_function():

    SETUP_CODE = '''
from __main__ import bubble_sort, bubble_sort2
from random import shuffle'''
 
    TEST_CODE = '''
ku = [x for x in range(100)]
shuffle(ku)
bubble_sort(ku)
'''

    TEST_CODE2 = '''
ku = [x for x in range(100)]
shuffle(ku)
bubble_sort2(ku)
'''
                
    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 100)
    
    times2 = timeit.repeat(setup = SETUP_CODE,
                        stmt = TEST_CODE2,
                        repeat = 3,
                        number = 100)
 
    # priniting minimum exec. time
    print('Bubble sort  time: {}'.format(min(times)))
    print('Bubble sort2  time: {}'.format(min(times2)))
 



if __name__ == '__main__':
    doctest.testmod(verbose=True)
    Time_function()
 