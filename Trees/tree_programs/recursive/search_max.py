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
maxdata = float("-inf")
def maxData_rec(node): 
    global maxdata
    #base case
    if not node:
        return maxdata

    #recursion case
    else:
        if node.data > maxdata:
            maxdata = node.data
        maxData_rec(node.left)
        maxData_rec(node.right)

        return maxdata
    
print(maxData_rec(root))