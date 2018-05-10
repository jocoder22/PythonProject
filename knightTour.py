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


def genLegalMoves(x, y, bdsize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdsize) and legalCoord(newY, bdsize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdsize):
    if x >= 0 and x < bdsize:
        return True
    else:
        return False


def KnightTour(n, path, u, limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = KnightTour(n+1, path, nbrList[i], limit)
            i = i + 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done
