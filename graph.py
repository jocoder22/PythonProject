#!/usr/bin/env python
import doctest
'''
python -i <file_name.py>.
The above will keep your session running and will monitor for code changes.
'''


class Vertex:
    '''
    This is the implementation of the vertex class.

    '''

    def __init__(self, key):
        self.id = key
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
        return str(self.id) + " connected to: " + str(
            [x.id for x in self.connectedTo])
        # return "{} connected to: {}".format(self.id,
        #                                    [x.id for x in self.connectedTo])


class Graph:
    '''
    This is the implementation of Graph class.

    '''

    def __init__(self):                              
        self.vertList = {}                           
        self.numVertices = 0                                        
                                                   
    def addVertex(self, key):                       
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def getAllVertices(self):
        return self.vertList.keys()

    def addEdge(self, vfrom, vto, weight=0):
        if vfrom not in self.vertList:
            self.addVertex(vfrom)
        if vto not in self.vertList:
            self.addVertex(vto)

        self.vertList[vfrom].addNeighbor(self.vertList[vto], weight)

    def __iter__(self):
        return iter(self.vertList.values())

    def __contains__(self, n):
        return n in self.vertList


g = Graph()
for i in range(6):
    g.addVertex(i)

g.addEdge(0, 1, 7)
g.addEdge(0, 2, 12)
g.addEdge(1, 2, 10)
g.addEdge(1, 3, 9)
g.addEdge(2, 4, 35)
for vertex in g:
    print(vertex)
    print(vertex.getConnections())
    print('\n')

if __name__ == '__main__':
    doctest.testmod(verbose=True)
