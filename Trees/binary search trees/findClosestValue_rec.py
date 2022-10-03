#Recursive approach for finding the element from BST that is closest to the given key
#Time complexity = O(logn), because it only searches the half of the tree


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
#               11  13

def findClosest(root, key):
    if not root:
        return None

    if root.data == key:
        return root

    if key < root.data:
        if root.left == None:
            return root
        
        else:
            temp = findClosest(root.left, key)
            if (abs(temp.data - key) > abs(root.data - key)):
                return root
            else:
                return temp

    elif key > root.data:
        if root.right == None:
            return root

        else:
            temp = findClosest(root.right, key)
            if(abs(temp.data - key) > abs(root.data - key)):
                return root
            else:
                return temp


print(findClosest(root, 5).data)