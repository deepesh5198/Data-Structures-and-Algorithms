#given a BST find the minimum element in BST
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

def findMinimumRec(root):
    if not root:
        return
    else:
        current_node = root
        if current_node.left is not None:
            return findMinimumRec(current_node.left)

        else:
            return current_node.data


print("find Min. Recursively: ", findMinimumRec(root))


def findMinimumIter(root):
    if not root:
        return
    else:
        current_node = root
        while current_node is not None:
            current_node = current_node.left

        return current_node.data

print("find Min. Iteratively: ", findMinimumRec(root))