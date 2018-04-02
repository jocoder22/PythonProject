
#!/usr/bin/env python
import doctest
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
    >>> arr2 = [15,3,18,4,5,90,23,14,20]
    >>> bubble_sort(arr2)
    >>> bubble_sort(arr)
    >>> arr
     
    >>> arr2
     
    '''
    # for every element arranged backward
    for n in range(len(arr)-1,0,-1):
        # the point to swtich
        for k in range(n):
            if arr[k] > arr[k +1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp


if __name__ == '__main__':
    doctest.testmod(verbose=True)