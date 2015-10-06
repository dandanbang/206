#---------------------------------------------------------
# <Daniel Wei-Hsuan Chen>
# <daniel@ischool.berkeley.edu>
# Homework #2
# September 19, 2015
# main.py
# Main
#---------------------------------------------------------
from __future__ import print_function
from BST import *
import string
import re

def promptUser():
    "Prompts user to enter search word"
    userInput = str(raw_input("Query?"))
    return userInput.lower()

def loadText():
    "loads the Pride and Prejudice text from local"
    with open ("/Users/dandanbang/Desktop/Pride and Prejudice.txt", "r") as myfile:
        text = myfile.read()
    return text

def split(rawText):
    "split the text by whitespace and newline"
    rawText = rawText.lower()
    text_split = re.split(r'[ \t\n]+', rawText)
    return text_split

def clean(raw):
    """takes an input of a list of text and then return a clean text by removing digits
        and punctuations and also making text lowercase"""
    list1 = []
    list2 = []
    for word in raw:
        list1.append("".join(s for s in word if not s.isdigit()))
    for word in list1:
        list2.append("".join(s for s in word if s.isalpha()))
    return list2

def loadTree(text, tree):
    "load the text into the tree"
    for token in text:
        tree.add(token)
    return tree

def main():
    raw = loadText() #loading the text into raw
    splitText = split(raw)
    text = clean(splitText) #removing digits and punctuation
    rawTree = BSTree() #creates a tree
    loadedTree = loadTree(text, rawTree) #dump the text into the Binary Tree
    userInput = promptUser()
    while userInput != "terminate":
        if userInput == "stats":
            print('The number of entries: ' + str(loadedTree.size()))
            print('The maximum depth: ' + str(loadedTree.height()))
        else:
            print('The word ' + str(userInput) + ' appears ' + str(loadedTree.find(userInput)) + ' times in the tree.' )
        userInput = promptUser()

if __name__ == "__main__":
    main()    