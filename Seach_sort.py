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



if __name__ == '__main__':
    doctest.testmod(verbose=True)