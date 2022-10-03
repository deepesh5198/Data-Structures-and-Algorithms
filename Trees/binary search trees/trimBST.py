#Problem: given two values Min and Max trim the BST such that only values in the resulting tree are
#from Min to Max values

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left  = None
        self.right = None

root = BSTNode(10)
root.left = BSTNode(7)
root.right = BSTNode(15)
root.left.left = BSTNode(3)
root.left.right = BSTNode(9)
root.right.left = BSTNode(12)
root.right.right = BSTNode(17)
root.right.left.left = BSTNode(11)
root.right.left.right = BSTNode(13)

#              10
#             /   \
#            7      15
#           / \    /  \
#          3   9  12   17
#                /  \
#               11  13

def traverseInorder(root):
    if not root:
        return 

    else:
        traverseInorder(root.left)
        print(root.data)
        traverseInorder(root.right)

def trimthisBST(root, a, b):
    if not root:
        return
    
    root.left = trimthisBST(root.left, a, b)
    root.right = trimthisBST(root.right, a, b)
    if a <= root.data <= b:
        return root

    elif root.data < a:
        return root.right

    elif root.data > b:
        return root.left





newroot = trimthisBST(root, 3,10)
traverseInorder(newroot)