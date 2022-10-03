#given a BST find the Predecessor of X
#If X has two children then its inorder predecessor is the maximum value in its left subtree.
# if it does not have a left child then node's inorder predecessor is its first left ancestor. 

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

def findPredecessorOf(X):
    temp = None
    if X.left is not None:
        temp = X.left
        while temp.right is not None:
            temp = temp.right
        return temp.data
    return None


print("Predecessor of 12 is : ", findPredecessorOf(root.right.left))
