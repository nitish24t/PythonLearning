from Stack import Stack
from Queue import Queue

"""Node class for Binary Tree"""
class btNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

"""Binary Tree Class"""
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.level = 0

    """Recursive Insert node in BST"""
    def RecursiveInsertNode(self,data,rootnode):
        if rootnode is None:
            print("one---")
            rootnode = btNode(data)
            self.size += 1
            print(self.size," node entered at root1 ",data)
        else:
            if data > rootnode.data:
                print("two")
                if rootnode.right is None:
                    rootnode.right = btNode(data)
                    self.size += 1
                    print(self.size," node entered at root.right ",data)
                else:
                    self.RecursiveInsertNode(data,rootnode.right)
            if data < rootnode.data:
                print("three")
                if rootnode.left is None:
                    rootnode.left = btNode(data)
                    self.size += 1
                    print(self.size," node entered at root.left ",data)
                else:
                    self.RecursiveInsertNode(data,rootnode.left)

    """Iterative Insert node in BST"""
    def IterativeInsertNode(self,data):
        if self.root is None:
            self.root = btNode(data)
            self.size += 1
            print(self.size," node entered at root ",data)
        else:
            troot = self.root
            while True:
                if troot.left != None:
                    if data < troot.data:
                        troot = troot.left
                if troot.left == None and data < troot.data:
                    troot.left = btNode(data)
                    self.size += 1
                    print(self.size," node entered left ",data)
                    break

                if troot.right != None:
                    if data > troot.data:
                        troot = troot.right
                if troot.right == None and data > troot.data:
                    troot.right = btNode(data)
                    self.size += 1
                    print(self.size," node entered right ",data)
                    break

def height(root):
    if isleaf(root):
        return 0
    return 1 + max(height(c) for c in children(root))

"""Return True if node is Leaf Node"""
def isleaf(root):
    return not root.left and not root.right


"""left to right children"""
def children(parent):
    if parent.left:
        yield parent.left
    if parent.right:
        yield parent.right

"""right to left children"""
def children1(root):
    if root.right:
        yield root.right
    if root.left:
        yield root.left

"""Preorder recursive traversal"""
def preorderRecursiveTraversal(root):
    print(root.data,end = " ")
    for c in children(root):
        preorderRecursiveTraversal(c)

"""Preorder iterative traversal"""
def preorderIterativeTraversal(root):
    st = Stack()
    st.push(root)
    while not st.isEmpty():
        node = st.pop()
        print(node.data,end=" ")
        for c in children1(node):
            st.push(c)

"""Postorder recursive traversal"""
def postorderRecursiveTraversal(root):
    for c in children(root):
        postorderRecursiveTraversal(c)
    print(root.data,end=" ")

"""Postorder iterative traversal"""
def postOrderIterativeTraversal(root):
    stack1 = Stack()
    stack1.push(root)

    stack2 = Stack()
    while not stack1.isEmpty():
        node = stack1.pop()
        stack2.push(node)
        for c in children(node):
            stack1.push(c)

    #Just printing stack
    while not stack2.isEmpty():
        print(stack2.pop().data,end=" ")

"""Inorder Recursive traversal"""
def inordreRecursiveTraversal(root):
    if root.left:
        inordreRecursiveTraversal(root.left)
    print(root.data,end=" ")
    if root.right:
        inordreRecursiveTraversal(root.right)

"""Inorder Iterative traversal"""
def inordreIterativeTraversal(root):
    st = Stack()
    st.push(root)
    current = root.left
    while not st.isEmpty() or current != None:
        if current != None:
            st.push(current)
            current = current.left
        else:
            node = st.pop()
            print(node.data,end=" ")
            current = node.right

"""Level Order Traversal"""
def levelOrderTraversal(root):
    qu = Queue()
    qu.enqueue(root)
    while not qu.isEmpty():
        node = qu.dequeue()
        print(node.data,end=" ")
        if node.left:
            qu.enqueue(node.left)
        if node.right:
            qu.enqueue(node.right)

def spiralTraversal(root):
    st1 = Stack()
    st2 = Stack()
    st1.push(root)

    while not st1.isEmpty() or not st2.isEmpty():
        while not st1.isEmpty():
            node = st1.pop()
            print(node.data,end=" ")
            if node.right:
                st2.push(node.right)
            if node.left:
                st2.push(node.left)

        while not st2.isEmpty():
            node = st2.pop()
            print(node.data, end=" ")
            if node.left:
                st1.push(node.left)
            if node.right:
                st1.push(node.right)

"""MAIN method"""
if __name__ == "__main__":
    bt = BinaryTree()
    bt.IterativeInsertNode(5)
    bt.IterativeInsertNode(10)
    bt.IterativeInsertNode(15)

    bt.RecursiveInsertNode(2,bt.root)
    bt.RecursiveInsertNode(4,bt.root)
    bt.RecursiveInsertNode(8,bt.root)
    bt.RecursiveInsertNode(9,bt.root)
    bt.RecursiveInsertNode(15,bt.root)

    print("\nrecursive preorder")
    preorderRecursiveTraversal(bt.root)
    print("\niterative preorder")
    preorderIterativeTraversal(bt.root)
    print("\nrecursive Postorder")
    postorderRecursiveTraversal(bt.root)
    print("\niterative postorder")
    postOrderIterativeTraversal(bt.root)
    print("\ninorder Recursive Traversal")
    inordreRecursiveTraversal(bt.root)
    print("\ninorder Iterative Traversal")
    inordreIterativeTraversal(bt.root)
    print("\nlevel order traversal")
    levelOrderTraversal(bt.root)
    print("\nSpiral Traversal")
    spiralTraversal(bt.root)

    print("\nheight of tree : ",height(bt.root))
