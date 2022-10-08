from logging import root


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




ptr = 0
def diameterOfTree(root):
    global ptr
    if not root:
        return 0
    left = diameterOfTree(root.left)
    right = diameterOfTree(root.right)

    if left + right > ptr:
        ptr = left + right

    return max(left,right)+1

print(diameterOfTree(root))
    
    