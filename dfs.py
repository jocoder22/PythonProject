#!/usr/bin/env python

from graph2 import State, Node, Graph

graph = {'A' : set(['B', 'C']),
         'B' : set(['A', 'D', 'F']),
         'C' : set(['A', 'F']),
         'D' : set(['B']),
         'E' : set(['B', 'F']),
         'F' : set(['C', 'E'])}


def dfsearch(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

    if vertex not in visited:
        visited.add(vertex)

        stack.extend(graph[vertex] - visited)
        
    return visited