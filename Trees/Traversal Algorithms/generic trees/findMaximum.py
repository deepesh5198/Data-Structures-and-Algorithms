#given a BST find the maximum element in BST
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

def findMaximumRec(root):
    if not root:
        return
    else:
        current_node = root
        if current_node.right is not None:
            return findMaximumRec(current_node.right)

        else:
            return current_node.data


print("find Max. Recursively: ",findMaximumRec(root))

def findMaximumIter(root):
    if not root:
        return

    else:
        current_node = root
        while current_node.right is not None:
            current_node = current_node.right

        return current_node.data
print("find Max. Iteratively: ", findMaximumIter(root))
