#!/usr/bin/env python
from Graph import Graph


def KnightGraph(bdsize):
    ktGraph = Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            nodeId = postToNodeId(row, col, bdsize)
            newPositions = genLegalMoves(row, col, bdsize)
            for e in newPositions:
                nid = postToNodeId(e[0], e[1], bdsize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def postToNodeId(row, column, board_size):
    return (row * board_size) + column

