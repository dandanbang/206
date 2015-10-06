#---------------------------------------------------------
# <Daniel W. Chen>
# <daniel@ischool.berkley.edu>
# Homework #2
# September 15, 2015
# BST.py
# BST
#---------------------------------------------------------
from __future__ import print_function

class Node:
    #Constructor Node() creates node
    def __init__(self,word):
        self.word = word
        self.right, self.left = None, None
        self.count, self.depth = 1, 0
    
class AVLTree:
    def __init__(self, root=None):
        "Constructor"
        self.root = root
        self.maxDepth = 1
        self.entry = 0

    def find(self, word):
        "find the words by calling internal function"
        return _find(self.root, word)
    
    def add(self, word):
        "add a node to the current tree"
        if not self.root: #If the tree is currently empty. assign the root arrow to the new word by creating new Node
            self.root = Node(word)
            self.entry = 1
            return
        self.entry = _add(self.root, self.root, word, self.entry) #If it's not empty, let's call the internal method to add the word!

    def inOrderPrint(self):
        "print the nodes with the in order rule"
        _inOrderPrint(self.root)

    def size(self):
        "return the number of nodes in the tree"
        return self.entry

    def height(self):
        "return the height of the tree"
        return self.maxDepth

#Internal Functions
def _add(headRoot, root, word, entry):
    """add the word to the tree, if it exists then add counts to the word, also the function updates
        the height and number of nodes in the tree"""
    if root.word == word: #If the word equals the current root word, then add one to the count
        root.count += 1
        return entry
    if root.word > word: #If the input word is smaller than the current root word
        if root.left == None and root.right == None:
            _updateDepth(headRoot, word)
        if root.left == None: #if the current root.left is empty. add the word by creating a new node!
            root.left = Node(word)
        else:
            return _add(headRoot, root.left, word, entry) #if it's not empty, we will to recursively call the function itself by using the root.left node
    else:
        if root.right == None and root.left == None:
            _updateDepth(headRoot, word)
        if root.right == None: #If the input word is bigger than the current root word and the right node is empty, add!
            root.right = Node(word)
        else:
            return _add(headRoot, root.right, word, entry) #If not empty, we will have to recursively call itself by passing in the root.right node
    
def _find(root, word):
    "find the word and return the count of the word"
    if root == None:
        return 0
    if root.word == word: #If the word equals the current word, we need to return the count of the word
        return root.count, root.depth
    if root.word > word: #If the input word is smaller than the current root word
        return _find(root.left, word)
    else:
        return _find(root.right, word)
    
def _isDuplicate(root, word):
    if (_find(root, word) != 0):
        return False

def _updateDepth(root, word):
    if root.word == word: #If the word equals the current word, we need to return the count of the word
        return
    if root.word > word: #If the input word is smaller than the current root word
        print('have i been here?')
        print(root.word)
        root.depth += 1
        return _find(root.left, word)
    else:
        root.depth += 1
        return _find(root.right, word)

def _inOrderPrint(root):
    if not root:
        return
    _inOrderPrint(root.left)
    print (root.word)
    print (root.count)
    _inOrderPrint(root.right)