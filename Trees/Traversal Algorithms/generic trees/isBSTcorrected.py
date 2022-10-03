#THiS approach is WRONG!!

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

def findmax(root):
    if not root:
        return
    else:
        while root.right != None:
            root = root.right
        return root.data

def findmin(root):
    if not root:
        return
    else:
        while root.left != None:
            root = root.left
        return root.data

def isBST(root):
    if root is None:
        return 1

    else:
        if (root.left != None and findmax(root.left) > root.data)\
             or (root.right != None and findmin(root.right) < root.data):
            return 0
        else:
            return isBST(root.left) and isBST(root.right)

print(isBST(root))
