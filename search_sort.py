#!/usr/bin/env python
import doctest
'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''

def seq_search(arr, ele):
    '''
    This function return true if ele is found in arr
     
    Input: List
     
    Output: Boolean
     
    Test:
    >>> arr1 = [1, 3, 5, 6, 9]
    >>> seq_search(arr1, 5)
    True
    >>> seq_search(arr1, 8)
    False
    >>> seq_search(arr1, 9)
    True
    '''
    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == ele:
            found = True
        else:
            pos += 1

    return found



def sorted_seq_search(arr, ele):
    '''
    This function does sorted sequential search
     
    Input: List
     
    Output: Boolean
     
    Test:
    >>> mylist1 = [7,2,9,5,3,1,29,35]
    >>> sorted_seq_search(mylist1, 29)
    True
    >>> mylist2 = [7,3,9,1,4,9,35,31,29]
    >>> sorted_seq_search(mylist2, 37)
    False
    >>> sorted_seq_search(mylist2, 2)
    False
    '''
    pos = 0
    found = False
    stopped = False
    arr.sort()

    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                stopped = True

            else:
                pos += 1
    return found



def binary_search(arr, ele):
    # first and last index values
    first = 0
    last = len(arr)

    found = False

    while first <= last and not found:
        mid = (first + last) // 2 

        # match found
        if arr[mid] == ele:
            found = True

        # set new midpoint up or down depending on comparison
        


if __name__ == '__main__':
    doctest.testmod(verbose=True)