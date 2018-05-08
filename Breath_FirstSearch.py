#!/usr/bin/env python


def breathfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVent = vertQueue.dequeue()
        for nbr in currentVent.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVent.getDistance() + 1)
                nbr.setPred(currentVent)
                vertQueue.enqueue(nbr)
        currentVent.setColor('black')