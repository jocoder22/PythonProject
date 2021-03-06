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


# Here cities are arranged in increasing distance from the originating city
travel = {'New York' : set(['Newark', 'Baltimore','Dallars', 'Houston']),
          'Baltimore' : set(['Newark', 'Orlando']),
          'Newark' : set(['New York', 'Orlando', 'Atlanta']),
          'Dallars' : set(['Houston', 'Atlanta' , 'Newark']),
          'Houston' : set(['New York']),
          'Orlando' : set(['New York', 'Atlanta']),
          'Atlanta' : set(['Baltimore', 'Houston'])}


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

list(bfs_path(graph, 'A', 'F'))
list(bfs_path(graph2, 'C', 'G'))

list(bfs_path(travel, 'New York', 'Atlanta'))
list(bfs_path(travel, 'Atlanta', 'New York'))

shortest_path(travel, 'Baltimore', 'Houston')
shortest_path(travel, 'Atlanta', 'New York')

