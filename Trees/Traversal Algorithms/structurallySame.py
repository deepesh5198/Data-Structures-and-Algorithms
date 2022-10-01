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

root2 = Tree(10)
root2.left = Tree(20)
root2.right = Tree(30)
root2.right.left = Tree(31)
root2.right.right = Tree(32)
root2.left.left = Tree(40)
root2.left.right = Tree(50)

def structurallySame(root1, root2):
    if (not root1.left) and (not root1.right) and (not root2.left) and (not root2.right)\
        and root1.data == root2.data:
        return True 

    elif (root1.data != root2.data) or (root1.left and not root2.left) or\
        (root1.right and not root2.right) or (not root1.left and root2.left) or\
            (not root1.right and root2.right):
        return False

    left = structurallySame(root1.left, root2.left) if root1.left and root2.left else True
    right = structurallySame(root1.right, root2.right) if root1.right and root2.right else True

    return left and right

print(structurallySame(root1, root2))