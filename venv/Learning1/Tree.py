
class Node:
    def __init__(self,data,parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def children(self,parent):
        if parent.left:
            return parent.left
        if parent.right:
            return parent.right

    def preorderTraversal(self,root):
        print(root.data)
        for c in self.children(root):
            preorderTraversal(c)
            print(c.data)








