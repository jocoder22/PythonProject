#!/usr/bin/env python
import doctest
'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''

MyTree = ['a', # root                                        [a]
           ['b',   # left subtree                           /   \
            ['d', [], []],          #                      /     \
            ['e', [], []]          #                      /       \
           ],                       #                   [b]       [c]
           ['c',   # right subtree                     /   \       |
            ['f', [], []], #                          /     \      |
            []                     #                [e]     [d]   [f]
           ]
         ]


def BinaryTree(r):
    return [r, [], []]


def insertLeftChild(root, newbranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newbranch,t,[]])
    else:
        root.insert(1,[newbranch,[],[]])
    return root


def insertRightChild(root, newbranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newbranch,[],t])
    else:
        root.insert(2,[newbranch,[],[]])
    return root



         
if __name__ == '__main__':
    doctest.testmod(verbose=True)