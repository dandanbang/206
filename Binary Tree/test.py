#---------------------------------------------------------
# <Daniel Wei-Hsuan Chen>
# <daniel@ischool.berkeley.edu>
# Homework #2
# September 19, 2015
# test.py
# test
#---------------------------------------------------------

from BST import *
from hw2 import *

testTree = BSTree()
#Functions for use
testTree.add('5')
testTree.add('4')
testTree.add('3')
testTree.add('8')
testTree.inOrderPrint()
testTree.add('7')
testTree.add('2')
testTree.add('2')
print(testTree.entry)
print(testTree.size())
testTree.find('2')
testTree.add('9')
testTree.find('2')

#print(testTree.find('5'))
testTree2 = BSTree()
testTree2.add(5)
testTree2.add(2)
testTree2.add(1)
testTree2.add(1)
testTree2.add(1)
testTree2.add(2)
testTree2.add(2)
testTree2.add(5)
print(testTree2.entry)
print(testTree2.size())
testList = [5, 2, 1, 6, 8, 91, 91, 91, 91]
testTree3 = BSTree()
for number in testList:
    testTree3.add(number)
print(testTree3.size())
print(testTree3.height())
testTree3.add(7)
print(testTree3.size())
print(testTree3.height())
print(str(testTree3.find(91)))
testTree4 = BSTree()
testList2 = [5, 2, 1, 6, 8, 91, 91, 91, 91, 'dd', 'aaad', 'adad', '', '']
print(testTree4.size())
print(testTree4.height())
print(testTree3.find('dd'))
print(testTree3.height())
testTree3.inOrderPrint()
testTree4.inOrderPrint()


main()