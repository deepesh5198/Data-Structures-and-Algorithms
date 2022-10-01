#Problem26: checks if Tree2 is a mirror Tree of Tree1
####Not working!####

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
 

def mirrorThisTree(root):
    if not root:
        return

    else:
        mirrorThisTree(root.left)
        mirrorThisTree(root.right)
        temp = root.left
        root.left = root.right
        root.right =temp

    return root

root2 = mirrorThisTree(root1)

def areMirrorTrees(root1,root2):
    if (root1 == None and root2 == None):
        return True

    elif (root1 == None or root2 == None):
        return False
        
    elif(root1.data == root2.data):
        return True

    elif (root1.data != root2.data):
        return False

    else:
        return areMirrorTrees(root1.left, root2.right) and areMirrorTrees(root1.right, root2.left) 


print(areMirrorTrees(root1, root2))
