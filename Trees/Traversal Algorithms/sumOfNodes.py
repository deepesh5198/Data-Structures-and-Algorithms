class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root1 = Tree(1)
root1.left = Tree(2)
root1.right = Tree(3)
root1.right.left = Tree(4)
root1.right.right = Tree(5)
root1.left.left = Tree(6)
root1.left.right = Tree(7)
root1.left.left.left = Tree(8)
root1.left.left.right = Tree(9)
root1.left.left.left.left = Tree(10)

def sumofAllNodesinTree(root):
    if not root:
        return 0

    else:
        return root.data + sumofAllNodesinTree(root.left) + sumofAllNodesinTree(root.right)


print(sumofAllNodesinTree(root1))