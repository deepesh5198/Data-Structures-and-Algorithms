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

def isBST(root, min, max):
    if root is None:
        return 1

    else:
        if (root.data <= min or root.data >= max):
            return 0
        else:    
            result = isBST(root.left, min, root.data)
            result = result and isBST(root.right, root.data, max)
            return result

print(isBST(root, float("-inf"), float("inf")))
