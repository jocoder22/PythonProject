#!/usr/bin/env python

from graph2 import State, Node, Graph

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



def dfsearch(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)

            stack.extend(graph[vertex] - visited)

    return visited


def dfsearch2(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for nxt in graph[start] - visited:
        dfsearch2(graph, nxt, visited)
    
    return visited


def dfs_path(graph, start, goal):
    stack = [(start, [start])]

    while stack:
        (vertex, path) = stack.pop()

        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))

dfs_path(graph, 'A', 'F')



        