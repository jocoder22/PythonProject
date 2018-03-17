#!/usr/bin/env python
import doctest
'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''


def permute(s):
    '''
    This function returns the permutation of a given string
     
    Input: string
    Output: string
     
    Test: 
    >>> permute('AFG')
    ['AFG', 'AGF', 'FAG', 'FGA', 'GAF', 'GFA']
    >>> permute('123')
    ['123', '132', '213', '231', '312', '321']
    >>> permute('E T')
    ['E T', 'ET ', ' ET', ' TE', 'TE ', 'T E']
    '''
    out = []
    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i + 1:]):
                out += [let+perm]
    
    return out

print(permute('ABC'))

if __name__ == '__main__':
    doctest.testmod(verbose=True)

# if __name__ == '__main__':
# 	doctest.testmod(verbose=True)