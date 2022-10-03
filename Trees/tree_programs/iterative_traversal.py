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
    result = []
    if not node:
        return

    stack = []
    stack.append(node)
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
print(preorder(root))

#########################################################
#2. InOrder
print("*"*80)
print("Inorder")
def inorder(node):
    result = []
    if not node:
        return

    stack = []
    while stack or node:
        if node:
            stack.append(node)     
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right

    return result
    
print(inorder(root))

#########################################################
#3. PostOrder
print("*"*80)
print("postorder")
def postorder(node):
    result = []
    visited = set()
    stack = []

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right

            else:
                visited.add(node)
                result.append(node.data)
                node =None
    return result
print(postorder(root))