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

count = 0 
def kthLargestinBST(root, k): 
    global count 
    if not root: 
        return None; 
    else:
        right = kthLargestinBST(root.right, k) 
        if right is not None: 
            return right
        else:
            count += 1 
            if count == k: 
                return root.data 
            return kthLargestinBST(root.left, k)

print(kthLargestinBST(root, k=2))