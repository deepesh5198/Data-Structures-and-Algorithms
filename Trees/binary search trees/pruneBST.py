#problem 90: given a BST and two integer values Min and Max, Prune the BST such that elements that are not in Min-Max
#range are not in the resulting tree

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


def pruneBST(root, Min, Max):
    if not root:
        return
    else:
        root.left = pruneBST(root.left, Min, Max)
        root.right = pruneBST(root.right, Min, Max)
        
        if Min <= root.data <= Max:
            return root

        if root.data < Min:
            return root.right

        if root.data > Max:
            return root.left

def inorderTraversal(root):
    if not root:
        return

    else:
        inorderTraversal(root.left)
        print(root.data)
        inorderTraversal(root.right)

        
pruned_tree = pruneBST(root, 3,11)
inorderTraversal(pruned_tree)