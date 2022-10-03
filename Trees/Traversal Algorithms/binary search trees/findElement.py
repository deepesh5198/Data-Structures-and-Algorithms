#given a BST and an element return if True if the element present in BST
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

def findElement(root, data):
    if not root:
        return 0
    else:
        current_node = root
        while current_node is not None:
            if data == current_node.data:
                return 1
            if data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return 0

print(findElement(root, 9))