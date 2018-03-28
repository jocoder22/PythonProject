#!/usr/bin/env python
import doctest
'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''


class HashTable(object):

    def __init__(self, size):

        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key




if __name__ == '__main__':