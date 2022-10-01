from platform import node


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

def deleteTree(node):
    if not node:
        return 

    else:
        deleteTree(node.left)
        deleteTree(node.right)
        del node

deleteTree(root)

