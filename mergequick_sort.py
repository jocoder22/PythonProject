#!/usr/bin/env python
import doctest
'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''

def merge_sort(arr):

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


if __name__ == '__main__':
    doctest.testmod(verbose=True)