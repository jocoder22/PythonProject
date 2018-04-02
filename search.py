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
    '''
    This function do a binary search 
     
    Input: List
     
    Output: Boolean
     
    Test:
    >>> blist = [9,4,8,2,5,7,34,22,18]
    >>> binary_search(blist, 34)
    True
    >>> binary_search(blist, 39)
    False
    >>> binary_search(blist, 2)
    True
    '''
    # first and last index values
    first = 0
    last = len(arr) - 1

    found = False
    arr.sort()

    while first <= last and not found:
        mid = (first + last) // 2 

        # match found
        if arr[mid] == ele:
            found = True

        # set new midpoint up or down depending on comparison
        else:
            if ele < arr[mid]:
                last = mid - 1

            else:
                first = mid + 1

    return found



def recursive_binarysearch(arr, ele):
    '''
    This function perform a recursive implementation of binary search
     
    Input: List
     
    Output: Boolean
     
    Test:
    >>> list2 = [9,4,8,2,5,7,34,22,18]
    >>> recursive_binarysearch(list2, 49)
    False
    >>> recursive_binarysearch(list2, 1)
    False
    >>> recursive_binarysearch(list2, 22)
    True
    >>> recursive_binarysearch(list2, 4)
    True
    '''
    arr.sort()

    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2

        if arr[mid] == ele:
            return True

        else:
            if ele < arr[mid]:
                return recursive_binarysearch(arr[:mid], ele)
            else:
                return recursive_binarysearch(arr[mid + 1:], ele)




if __name__ == '__main__':
    doctest.testmod(verbose=True)