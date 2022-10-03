#problem: given a BST remove all the half nodes from it
#half node is one which only has one child
# NON RECURSIVE METHOD

from os import remove


class Queue:
    def __init__(self):
        self.que = []
        self.size = 0

    def enqueue(self, item):
        self.que.append(item)
        self.size +=1

    def dequeue(self):
        if self.size <= 0:
            print("Queue Underflow!")

        else:
            item = self.que[0]
            self.que.remove(item)
            self.size -=1
            return item

    def show_queue(self):
        print(self.que)

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

#              10
#             /   \
#            7      15
#           / \    /  \
#          3   9  12   17
#                /  
#               11  

# in the given BST 12 is the Half Node remove its left or right node which makes it half node.

def removeHalfNodes(root):
    if not root:
        return 

    else:
        root.left = removeHalfNodes(root.left)
        root.right = removeHalfNodes(root.right)
        if root.left == None and root.right == None:
            return root
        if root.left == None:
            return root.right
        if root.right == None:
            return root.left

        return root     
    
tree_without_halfnodes = removeHalfNodes(root)

def traverseInorder(root):
    if not root:
        return
    else:
        traverseInorder(root.left)
        print(root.data)
        traverseInorder(root.right)

traverseInorder(tree_without_halfnodes)
