#!/usr/bin/env python

def unqID(lst):
    unique_id = 0

    for i in lst:
        unique_id ^= i
    
    return unique_id

unqID([1,2,3,1,2,2,4,5,6,6,5,4,2])