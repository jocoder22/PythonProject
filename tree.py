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
        preorder(tree.getRightChild())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


        

    
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

    def preorder(self):
        print(self.key)
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()

    def inorder(self):
        if self.leftchild:
            self.leftchild.inorder()
        print(self.key)
        if self.rightchild:
            self.rightchild.inorder()

    def postorder(self):
        if self.leftchild:
            self.leftchild.postorder()
        if self.rightchild:
            self.rightchild.postorder()
        print(self.key)


        

r = Binarytree('b')
r.getRootVal()
r.insertLeftChild('b-left')
tleft = r.leftchild
tleft.insertLeftChild('b-left-left')
r.insertRightChild('b-right')
tRight = r.rightchild
tRight.insertLeftChild('b-right-left')
r.getRightChild().getRootVal()




class BinHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                i * 2 + 1
    
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist)
        self.currentSize = len(alist)
        self.heapList = [0] + alist[i]
        while (i > 0):
            self.percDown(i)
            i = i - 1





##*************************************###
##  Binary Search Implementation       ###
##*************************************###


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()



class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChild(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeDate(self, key, value, leftChild, rightChild):
        self.key = key
        self.payload = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

            



if __name__ == '__main__':
    doctest.testmod(verbose=True)