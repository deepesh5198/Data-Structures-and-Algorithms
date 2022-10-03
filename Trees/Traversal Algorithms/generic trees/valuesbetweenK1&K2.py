#problem 68: given a BST and two numbers K1 and K2 find all the values from BST that come in
#range of K1 and K2

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left  = None
        self.right = None

root = BSTNode(10)
root.left = BSTNode(7)
root.right = BSTNode(15)
root.left.left = BSTNode(3)
root.left.right = BSTNode(9)
root.right.left = BSTNode(12)
root.right.right = BSTNode(17)
root.right.left.left = BSTNode(11)
root.right.left.right = BSTNode(13)

#              10
#             /   \
#            7      15
#           / \    /  \
#          3   9  12   17
#                /  \
#               11   13

traverse_list = []

def traverseInorder(root):
    global traverse_list
    if not root:
        return
    else:
        traverseInorder(root.left)
        traverse_list.append(root.data)
        traverseInorder(root.right)
    return traverse_list

def getvalues_inrange(root, k1, k2):
    if not root:
        return
    else:
        traverse_list = traverseInorder(root)
        result = [x for x in traverse_list if (k1 <= x <=k2)]
        return result

# print(traverseInorder(root))
print(getvalues_inrange(root, 10,15))