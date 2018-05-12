#!/usr/bin/env python

from graph2 import State, Node, Graph

graph = {'A' : set(['B', 'C']),
         'B' : set(['A', 'D', 'F']),
         'C' : set(['A', 'F']),
         'D' : set(['B']),
         'E' : set(['B', 'F']),
         'F' : set(['C', 'E'])}

