from Stack import Stack

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

first = Node(5)
first.left = Node(2)
first.right = Node(10)
first.left.right = Node(4)
#first.left.left = Node(1)
first.right.left = Node(8)
first.right.left.right = Node(9)
first.right.right = Node(15)

"""     BOUNDARY ORDER TRAVERSAL
            5
           /  \
          2    10
        /  \   / \
            4  8  15
                \
                 9
"""

def isLeafNode(root):
    i = 0
    if root.left: i += 1
    if root.right: i += 1
    return i == 0

def PrintLeftNodes(root):
    if root is None:
        return
    if not isLeafNode(root):
        print(root.data, end=" ")
    PrintLeftNodes(root.left)

def PrintLeafNodes(root):
    if root is None:
        return
    if isLeafNode(root):
        print(root.data, end=" ")
        return
    PrintLeafNodes(root.left)
    PrintLeafNodes(root.right)

def PrintRightNodes(root):
    if root is None:
        return
    PrintRightNodes(root.right)
    if not isLeafNode(root) :
        print(root.data,end=" ")

PrintLeftNodes(first)
print()
PrintLeafNodes(first)
print()
PrintRightNodes(first.right)
