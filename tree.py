#!/usr/bin/env python
from collections import deque
import doctest
'''
python -i <file_name.py>
The above will keep your session running
and will monitor for code changes
'''

# #**************************************####
# #    LIST IMPLEMENTATION OF TREE        ###
# #                                       ###
# ###########################################
# Tree Implementation as list of lists   ###


MyTree = ['a',          # root                               [a]
          ['b',   # left subtree                            /   \
           ['d', [], []],          # b                     /     \
           ['e', [], []]          # b                     /       \
           ],                       # b                 [b]       [c]
          ['c',   # right subtree                      /   \       |
           ['f', [], []],         # b                 /     \      |
           []                     # b               [e]     [d]   [f]
           ]
          ]


def BinaryTree(r):
    return [r, [], []]


def insertLeftChild(root, newbranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newbranch, t, []])
    else:
        root.insert(1, [newbranch, [], []])
    return root


def insertRightChild(root, newbranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newbranch, [], t])
    else:
        root.insert(2, [newbranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newval):
    return root[0] == root(newval)


def getLeftchildValue(root):
    return root[1]


def getRightchildValue(root):
    return root[2]


# ## Tree Traversal


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def inorder(tree):
    if tree is not None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


def postorder(tree):
    if tree is not None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


# Example implementation
r = BinaryTree(3)
insertLeftChild(r, 4)
insertRightChild(r, 5)


# #**************************************####
# #   OBJECT ORIENTATION PARADIGM         ###
# #     IMPLEMENTATION OF TREE            ###
# ###########################################
# Tree Implementation as class object    ###


class Binarytree(object):

    def __init__(self, rootobj):
        self.key = rootobj
        self.leftchild = None
        self.rightchild = None

    def insertLeftChild(self, newnode):
        if self.leftchild is None:
            self.leftchild = Binarytree(newnode)
        else:
            t = Binarytree(newnode)
            t = self.leftchild
            self.leftchild = t

    def insertRightChild(self, newnode):
        if self.rightchild is None:
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


# #*************************************###
# #  Binary Search Implementation       ###
# #*************************************###


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.rightChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChild():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                    self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftchild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.isRightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:  # node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeDate(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.
                                                leftChild,
                                                currentNode.leftChild.
                                                rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.isRightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeDate(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.
                                                leftChild,
                                                currentNode.rightChild.
                                                rightChild)

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem


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


mytree = BinarySearchTree()
mytree[3] = 'red'
mytree[4] = 'blue'


# ##*******************************************##
# ##     Tree Questions                       ###
# ##******************************************###

# ## Validate BST
# # Solution 1: using tree traversal method
# # Idea: Inorder traversal of the tree will produce a sorted list of values

tree_vals = []


def inorder_tras(tree):
    if tree is not None:
        inorder_tras(tree.getLeftChild())
        tree_vals.append(tree.getRootVal())
        inorder_tras(tree.getRightChild())


def validate_BST(tree):
    inorder_tras(tree)
    return tree_vals == sorted(tree_vals)


root = Binarytree(10)
root.insertLeftChild(2)
root.insertRightChild(18)
root.rightchild.insertLeftChild(14)
root.rightchild.insertRightChild(19)
root.leftchild.insertLeftChild(1)
root.leftchild.insertRightChild(5)


root2 = Binarytree(10)
root2.insertLeftChild(8)
root2.insertRightChild(30)
root2.rightchild.insertLeftChild(14)
root2.rightchild.insertRightChild(19)
root2.leftchild.insertLeftChild(1)
root2.leftchild.insertRightChild(12)


# Solution 2
# Tracking min and max values


class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val 
        self.left = None
        self.right = None


def tree_max(node):
    if not node:
        return float('-inf')
    maxleft = tree_max(node.left)
    maxright = tree_max(node.right)
    return max(node.key, maxleft, maxright)


def tree_min(node):
    if not node:
        return float('inf')
    minleft = tree_min(node.left)
    minright = tree_min(node.right)
    return min(node.key, minleft, minright)


def verifytree(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.key <= tree_min(node.right) and
       verifytree(node.left) and verifytree(node.right)):
        return True
    else:
        return False


root3 = Node(10, 'Hello')
root3.left = Node(7, 'Seven')
root3.right = Node(30, 'Thirty')

root4 = Node(14, 'Hello')
root4.left = Node(70, 'Seventy')
root4.right = Node(30, 'Thirty')
root4.left.left = Node(20, 'Twenty')


# ***********************************##
#    Print tree values              ##
# ***********************************##

class MyNode:
    def __init__(self, val=None):
        self.val = val 
        self.left = None
        self.right = None


def levelOrderPrint(tree):
    if not tree:
        return
    nodes = deque([tree])
    currentcount, nextcount = 1, 0
    while len(nodes) != 0:
        currentnode = nodes.popleft()
        currentcount -= 1
        print(currentnode.val,)
        if currentnode.left:
            nodes.append(currentnode.left)
            nextcount += 1
        if currentnode.right:
            nodes.append(currentnode.right)
            nextcount += 1
        if currentcount == 0:
            # print('\n')
            currentcount, nextcount = nextcount, currentcount


treeroot = MyNode(1)
Node(1)
treeroot.left = MyNode(2)
treeroot.right = MyNode(3)


# Binary Trim
# Trim the tree between the min and max inclusive

def trimBST(tree, minval, maxval):
    if not tree:
        return
    
    tree.left = trimBST(tree.left, minval, maxval)
    tree.right = trimBST(tree.right, minval, maxval)

    if minval <= tree.val <= maxval:
        return tree

    if tree.val < minval:
        return tree.right

    if tree.val > maxval:
        return tree.left


if __name__ == '__main__':
    doctest.testmod(verbose=True)