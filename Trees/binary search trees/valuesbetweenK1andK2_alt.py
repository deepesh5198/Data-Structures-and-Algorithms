#problem 69: given a BST and two numbers K1 and K2 find all the values from BST that come in
#range of K1 and K2

from re import L


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
root.right.left.right = BSTNode(13)

#              10
#             /   \
#            7      15
#           / \    /  \
#          3   9  12   17
#                /  \
#               11   13

def getvalues_inrange(root, k1, k2):
    if not root:
        return
    
    else:
        q= Queue()
        temp = None
        q.enqueue(root)
        while q.size!=0:
            temp = q.dequeue()
            if k1 <= temp.data <= k2:
                print(temp.data)
                if temp.left != None and temp.left.data >= k1:
                    q.enqueue(temp.left)
                elif temp.right != None and temp.right.data <= k2:
                    q.enqueue(temp.right)

# print(traverseInorder(root))
getvalues_inrange(root, 3,10)