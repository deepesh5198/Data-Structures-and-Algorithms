from cmath import inf


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
#               11  13

def findClosest(root, key):
    difference = float("inf")
    if not root:
        return 0

    Q = Queue()
    Q.enqueue(root)
    while Q.size != 0:
        temp = Q.dequeue()
        if(difference > abs(temp.data - key)):
            difference = abs(temp.data - key)
            element = temp

            if temp.left != None:
                Q.enqueue(temp.left)

            if temp.right != None:
                Q.enqueue(temp.right)

    return element.data

print(findClosest(root, 12))