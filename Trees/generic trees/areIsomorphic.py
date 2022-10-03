class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root1 = Tree(10)
root1.left = Tree(20)
root1.right = Tree(30)
root1.right.left = Tree(31)
root1.right.right = Tree(32)
root1.left.left = Tree(40)
root1.left.right = Tree(50)
root1.left.left.left = Tree(60)
root1.left.left.right = Tree(70)
root1.left.left.left.left = Tree(88)

root2 = Tree(88)
root2.left = Tree(30)
root2.right = Tree(20)
root2.right.left = Tree(32)
root2.right.right = Tree(31)
root2.left.left = Tree(40)
root2.left.right = Tree(60)
root2.left.left.left = Tree(50)
root2.left.left.right = Tree(70)
root2.left.left.left.left = Tree(10)

def areIsomorphic(root1, root2):
    if (not root1 and not root2):
        return 1

    elif (not root1 and root2) or (root1 and not root2):
        return 0

    return (areIsomorphic(root1.left, root2.left) and areIsomorphic(root1.right, root2.right))


print(areIsomorphic(root1, root2))