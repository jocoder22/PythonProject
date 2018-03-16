#!/usr/bin/env python
import doctest
'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''


def permute(s):
    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i + 1:]):
                out += [let+perm]
    
    return out









if __name__ == '___main__':
    doctest.testmod()
