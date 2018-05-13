#!/usr/bin/env python

def bfsearch(graph, start):
    visited, queue = set(), [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] -visited)

    return visited



def bfs_path(graph, start, goal):
    queue = [(start, [start])]

    while queue:
        (vertex, path) = queue.pop(0)

        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                queue.append((nxt, path + [nxt]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_path(graph, start, goal))
    except StopIteration:
        return None