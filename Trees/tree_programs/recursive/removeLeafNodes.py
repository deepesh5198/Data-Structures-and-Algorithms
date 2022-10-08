#problem 89: given a binary tree remove the leaf nodes
#Solution: we can remove the leaf nodes by using Post Order Traversal method
from os import remove


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)
root.right.left = Tree(31)
root.right.right = Tree(32)
root.left.left = Tree(40)
root.left.right = Tree(50)
root.left.left.left = Tree(60)
root.left.left.right = Tree(70)

def removeLeafNodes(root):
    if not root:
        return

    else:
        if root.left == None and root.right == None:
            return None
        else:
            root.left = removeLeafNodes(root.left)
            root.right = removeLeafNodes(root.right)
        return root


def inorderTraversal(root):
    if not root:
        return

    else:
        inorderTraversal(root.left)
        print(root.data)
        inorderTraversal(root.right)
tree_without_leafs = removeLeafNodes(root)

inorderTraversal(tree_without_leafs)