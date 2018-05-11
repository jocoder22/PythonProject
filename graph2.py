#!/usr/bin/env python

from enum import Enum


class State(Enum):
    unvisited = 1  # White
    visited = 2  # Black
    visiting = 3  # Gray


class Node:

    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()

    def __str__(self):
        return str(self.num)
