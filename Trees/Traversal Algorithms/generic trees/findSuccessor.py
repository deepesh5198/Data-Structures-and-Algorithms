#given a BST find the Successor of X
#If X has two children then its inorder successor the minimum value in its right subtree. 

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

#              10
#             /   \
#            7      15
#           / \    /  \
#          3   9  12   17
#

def findSuccessorOf(X):
    temp = None
    if X.right is not None:
        temp = X.right
        while temp.left is not None:
            temp = temp.left
        return temp.data
    return None


print("Successor of 7 is : ", findSuccessorOf(root.left))
