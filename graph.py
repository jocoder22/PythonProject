#!/usr/bin/env python
import doctest
'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''

class vertex:
    
    def __init__(self, key):
        self.id = id
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr] 

    def __str__(self):
        return str(self,id) + " connected to: " + str([x.id for x in self.connectedTo])



if __name__ == '__main__':
    doctest.testmod(verbose=True)