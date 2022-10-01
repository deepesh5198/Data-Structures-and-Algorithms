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


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_at_left(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.left = self.left
            self.left = temp

    def insert_at_right(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right = self.right
            self.right = temp


def insertInBinaryTreeUsingLevelOrder(node, data):
    newNode = BinaryTree(data)
    if not node:
        node = newNode
        return node

    q= Queue()
    q.enqueue(node)

    node = None
    while not q.size == 0:
        node = q.dequeue()
        if data == node.data:
            return node
        if node.left is not None:
            q.enqueue(node.left)

        else:
            node.left = newNode
            return node

        if node.right is not None:
            q.enqueue(node.right)
        else:
            node.right = newNode
            return node

root = BinaryTree(10)
root.insert_at_left(20)
root.insert_at_left(30)
root.insert_at_left(40)
root.insert_at_right(60)


def preorder(node):
    if not node:
        return
    else:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
preorder(root)