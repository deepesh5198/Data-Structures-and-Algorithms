class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)
root.left.right = Tree(40)
root.left.left = Tree(50)
root.left.left.left = Tree(60)
root.left.left.right = Tree(70)


def findAllAncestors(root, node):
    if not root:
        return 0

    else:
        if (root.left.data == node or root.right.data == node or\
             findAllAncestors(root.left, node) or findAllAncestors(root.right, node)):
             print(root.data)
        return 1

findAllAncestors(root, 70)
