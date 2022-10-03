#given a BST insert the given Node such that it satisfies the BST

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

#              10
#             /   \
#            7      15
#           / \    /  \
#          3   9  12   17
#                /  
#               11  

def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)

        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)
    return root

node = BSTNode(13)

insertNode(root, node)
