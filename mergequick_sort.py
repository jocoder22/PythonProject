#!/usr/bin/env python
import doctest
'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''

def merge_sort(arr):
    '''
    This function performs merge sort  method
     
    Input: List
     
    Output: List
     
    Test:
    >>> arr = [5,3,8,4,5,90,23,14,2]
    >>> arr2 = [15,3,18,4,50,23,14,20,60]
    >>> merge_sort(arr2)
    >>> merge_sort(arr)
    >>> arr
    [2, 3, 4, 5, 5, 8, 14, 23, 90]
    >>> arr2
    [3, 4, 14, 15, 18, 20, 23, 50, 60]
    '''

    if len(arr) > 1:
        midd= len(arr)//2
        lefthalf = arr[:midd]
        righthalf = arr[midd:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i,j,k = 0,0,0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i,k = i + 1, k + 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j, k = j + 1, k + 1

    # print("Merging ", arr)



def quick_sort(arr):
    '''
    This function performs quick sort  method
     
    Input: List
     
    Output: List
     
    Test:
    >>> arr = [5,3,8,4,5,90,23,14,2]
    >>> arr2 = [15,3,18,4,50,23,14,20,60]
    >>> quick_sort(arr2)
    >>> quick_sort(arr)
    >>> arr
    [2, 3, 4, 5, 5, 8, 14, 23, 90]
    >>> arr2
    [3, 4, 14, 15, 18, 20, 23, 50, 60]
    '''

    quick_help(arr, 0, len(arr) - 1)

def quick_help(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)

        quick_help(arr, first, splitpoint-1)
        quick_help(arr, splitpoint+1, last)

def partition(arr, first, last):
    pivotvalue = arr[first]

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1
            
        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True

        else:
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]

    arr[first], arr[rightmark] = arr[rightmark], arr[first]

    return rightmark


if __name__ == '__main__':
    doctest.testmod(verbose=True)