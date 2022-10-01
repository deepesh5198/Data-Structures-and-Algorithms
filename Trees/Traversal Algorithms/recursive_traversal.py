#Pre-ordered traversal algo
#DLR, process data node, process left subtree and then process right sub tree

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

#########################################################
#Traversal Techniques
#1. PreOrder
print("Preorder")
def preorder(node):
    if not node:
        return
    else:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
    
preorder(root)

#########################################################
#2. InOrder
print("*"*80)
print("Inorder")
def inorder(node):
    if not node:
        return
    else:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
    
inorder(root)

#########################################################
#3. PostOrder
print("*"*80)
print("postorder")
def postorder(node):
    if not node:
        return
    else:
        postorder(node.left)
        postorder(node.right)
        print(node.data)
postorder(root)