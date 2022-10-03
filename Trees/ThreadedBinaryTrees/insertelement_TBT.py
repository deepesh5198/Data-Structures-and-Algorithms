#Inorder Threaded Traversal

class ThreadedBinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.Ltag = None
        self.Rtag = None


root = ThreadedBinaryTree(1)
root.Ltag = 1
root.left = ThreadedBinaryTree(5)
root.Rtag = 1
root.right = ThreadedBinaryTree(11)
root.left.Ltag = 1
root.left.left = ThreadedBinaryTree(2)
root.left.Rtag = 0
root.left.left.Rtag = 0

root.right.Ltag = 1
root.right.left = ThreadedBinaryTree(16)
root.right.Rtag = 1
root.right.right = ThreadedBinaryTree(31)
root.right.left.Ltag = 0
root.right.left.Rtag = 0
root.right.right.Ltag = 0
root.right.right.Rtag = 0


def insertRightTBT(P,Q):
    Q.right = P.right
    Q.Rtag = P.Rtag
    Q.left = P
    Q.Ltag = 0
    P.right = Q
    P.Rtag = 1
    if (Q.Rtag == 1):
        temp =  Q.right 
        while temp.Ltag:
            temp = temp.left

        temp.left = Q


Q = ThreadedBinaryTree(12)
Q.Rtag = 0
Q.Ltag = 0
insertRightTBT(root.right.right, Q )
    