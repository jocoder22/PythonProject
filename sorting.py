
#!/usr/bin/env python
import doctest
'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''

def bubble_sort(arr):
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