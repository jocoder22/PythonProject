#!/usr/bin/env python

def bfsearch(graph, start):
    visited, queue = set(), [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] -visited)

    return visited