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


def preorderPredecessor(P):
    if (P.Ltag == 0):
        return P.left

    else:
        position = P
        while position.Rtag == 0:
            position = position.right
    return position.right


def preorderTraversal(root):
    P = preorderPredecessor(root)
    while P!= root:
        P = preorderPredecessor(P)
        print(P.data)

preorderTraversal(root)
# print(preorderPredecessor(root))