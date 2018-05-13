#!/usr/bin/env python

graph = {'A' : set(['B', 'C']),
         'B' : set(['A', 'D', 'E']),
         'C' : set(['A', 'F']),
         'D' : set(['B']),
         'E' : set(['B', 'F']),
         'F' : set(['C', 'E'])}

graph2 = {'A' : set(['B', 'C']),
         'B' : set(['A', 'D', 'E']),
         'C' : set(['A', 'F']),
         'D' : set(['F', 'G']),
         'E' : set(['B', 'F']),
         'F' : set(['C', 'E']),
         'G' : set(['D','F'])}


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


# test cases
bfsearch(graph, 'A')
bfsearch(graph2, 'G')