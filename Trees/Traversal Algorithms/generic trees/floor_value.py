#problem 64: 

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
#               11   13


def floorinBST(root, data):
    if not root:
        return 
    else:
        if root.data == data:
            return root.data

        elif data < root.data:
            return floorinBST(root.left, data)

        floor = floorinBST(root.right, data)
        if floor <= data:
            return floor
        else: 
            return data


print(floorinBST(root,5))