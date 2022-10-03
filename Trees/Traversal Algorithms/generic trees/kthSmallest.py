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
def kthSmallestinBST(root, k): 
    global count 
    if(not root): 
        return None; 
    else:
        left = kthSmallestinBST(root.left, k) 
        if left is not None: 
            return left
        else:
            count += 1 
            if count == k: 
                return root.data 
            return kthSmallestinBST(root.right, k)

print(kthSmallestinBST(root, k=4))