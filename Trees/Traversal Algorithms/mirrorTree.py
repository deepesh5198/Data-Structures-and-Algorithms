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


def preorder(root):
    if not root:
        return

    else:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

preorder(root1)
print("#"*80)  

def mirrorThisTree(root):
    if not root:
        return 

    else:
        mirrorThisTree(root.left)
        mirrorThisTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
    return root

mirror = mirrorThisTree(root1)

preorder(mirror)