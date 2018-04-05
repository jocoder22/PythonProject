#!/usr/bin/env python
import doctest
'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''

def selection_sort(arr):
    '''
    This function performs selection sort method
     
    Input: List
     
    Output: List
     
    Test:
    >>> arr = [5,3,8,4,5,90,23,14,2]
    >>> arr2 = [15,3,18,4,50,23,14,20]
    >>> selection_sort(arr2)
    >>> selection_sort(arr)
    >>> arr
    [2, 3, 4, 5, 5, 8, 14, 23, 90]
    >>> arr2
    [3, 4, 14, 15, 18, 20, 23, 50]
    '''
    for slot in range(len(arr)-1,0,-1):
        # the length is reversed
        # looking for the maximium
        maxp = 0
        for location in range(1,slot+1):
            if arr[location] > arr[maxp]:
                maxp = location
        
        arr[slot], arr[maxp] = arr[maxp], arr[slot]

def selection_sort_desc(arr):
    '''
    This function performs selection sort descending method
     
    Input: List
     
    Output: List
     
    Test:
    >>> arr = [5,3,8,4,5,90,23,14,2]
    >>> arr2 = [15,3,18,4,50,23,14,20]
    >>> selection_sort_desc(arr2)
    >>> selection_sort_desc(arr)
    >>> arr
    [90, 23, 14, 8, 5, 5, 4, 3, 2]
    >>> arr2
    [50, 23, 20, 18, 15, 14, 4, 3]
    '''
    for slot in range(len(arr)-1,0,-1):
        # the length is reversed
        # looking for the maximium
        maxp = 0
        for location in range(1,slot+1):
            if arr[location] < arr[maxp]:
                maxp = location
        
        arr[slot], arr[maxp] = arr[maxp], arr[slot]


def insertion_sort(arr):
    '''
    This function performs insertion sort  method
     
    Input: List
     
    Output: List
     
    Test:
    >>> arr = [5,3,8,4,5,90,23,14,2]
    >>> arr2 = [15,3,18,4,50,23,14,20]
    >>> insertion_sort(arr2)
    >>> insertion_sort(arr)
    >>> arr
    [2, 3, 4, 5, 5, 8, 14, 23, 90]
    >>> arr2
    [3, 4, 14, 15, 18, 20, 23, 50]
    '''
    for i in range(1, len(arr)):
        currentvalue = arr[i]
        position = i

        while position > 0 and arr[position -1] > currentvalue:
            arr[position], position = arr[position -1], position - 1

        arr[position] = currentvalue



def shell_sort(arr):
    '''
    This function performs shell sort  method
     
    Input: List
     
    Output: List
     
    Test:
    >>> arr = [5,3,8,4,5,90,23,14,2]
    >>> arr2 = [15,3,18,4,50,23,14,20]
    >>> shell_sort(arr2)
    >>> shell_sort(arr)
    >>> arr
    [2, 3, 4, 5, 5, 8, 14, 23, 90]
    >>> arr2
    [3, 4, 14, 15, 18, 20, 23, 50]
    '''
    sublistcount = len(arr)//2

    while sublistcount > 0:
        for start in range(sublistcount):

            gap_insertion(arr, start, sublistcount)
        
        sublistcount = sublistcount/2



def gap_insertion(arr, start, gap):
    for i in range(start+gap, len(arr), gap):
        currentvalue = arr[i]
        position = i

        while position >= gap and arr[position-gap] > currentvalue:
            arr[position], position = arr[position-gap], position-gap

        arr[position] = currentvalue


if __name__ == '__main__':
    doctest.testmod(verbose=True)