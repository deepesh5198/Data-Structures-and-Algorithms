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


def sizeRecurrsive(node):
    if not node:
        return 0

    else:
        return sizeRecurrsive(node.left) + sizeRecurrsive(node.right) + 1

print(sizeRecurrsive(root))