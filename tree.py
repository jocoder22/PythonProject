#!/usr/bin/env python
import doctest
'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''

##**************************************####
##    LIST IMPLEMENTATION OF TREE        ###
##                                       ###
############################################
# Tree Implementation as list of lists   ###


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


def getRootVal(root):
    return root[0]

def setRootVal(root, newval):
    return root[0] == root(newval)


def getLeftchildValue(root):
    return root[1]

def getRightchildValue(root):
    return root[2]


### Tree Traversal

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())


    
# Example implementation
r = BinaryTree(3)
insertLeftChild(r,4)
insertRightChild(r, 5)



##**************************************####
##   OBJECT ORIENTATION PARADIGM         ###
##     IMPLEMENTATION OF TREE            ###
############################################
# Tree Implementation as class object    ###


class Binarytree(object):

    def __init__(self, rootobj):
        self.key = rootobj
        self.leftchild = None
        self.rightchild = None


    def insertLeftChild(self, newnode):
        if self.leftchild == None:
            self.leftchild = Binarytree(newnode)
        else:
            t = Binarytree(newnode)
            t = self.leftchild
            self.leftchild = t

    def insertRightChild(self, newnode):
        if self.rightchild == None:
            self.rightchild = Binarytree(newnode)
        else:
            t = Binarytree(newnode)
            t = self.rightchild
            self.rightchild = t

    def getRightChild(self):
        return self.rightchild
         
    def getLeftChild(self):
        return self.leftchild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key



r = Binarytree('b')
r.getRootVal()
r.insertRightChild('bx')
r.getRightChild().getRootVal()







if __name__ == '__main__':
    doctest.testmod(verbose=True)