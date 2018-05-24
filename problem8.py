#!/usr/bin/env python


class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value


INF = float("infinity")
NEG_INF = float("-infinity")


def isBST(tree, minval=NEG_INF, maxval=INF):
    if tree is None:
        return True

    if not minval <= tree.val <= maxval:
        return False

    return isBST(tree.left, minval, tree.val) and isBST(tree.right,
                                                        tree.val, maxval)


def isBST2(tree, lastNode=[NEG_INF]):
    if tree is None:
        return True

    if not isBST2(tree.left, lastNode):
        return False

    if tree.val < lastNode[0]:
        return False

    lastNode[0] = tree.val

    return isBST2(tree.right, lastNode)
