class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None: return 0
    return 1 + max(height(root.left),height(root.right))

def diameter(root):
    if root is None: return 0

    lht = height(root.left)
    rht = height(root.right)

    return max(lht + rht + 1,max(diameter(root.left),diameter(root.right)))

""" 
Constructed binary tree is  
                    1 
                  /   \ 
                2      3 
              /  \ 
            4     5
           /        \
         24          15
        /              \
       34               25 
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(24)
root.left.left.left.left = Node(34)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.left.right.right.right = Node(25)

print("diameter of binary tree is ",diameter(root))


"""Optimization"""
def height2(root,ans):
    if root is None: return 0

    lht = height2(root.left,ans)
    rht = height2(root.right,ans)
    ans[0] = max(ans[0],lht + rht + 1)
    return 1 + max(lht , rht)


def diameter2(root):
    if root is None: return 0
    ans = [-99999]
    ht_of_tree = height2(root,ans)
    return ans[0]

print("diameter2 of binary tree is ",diameter2(root))
