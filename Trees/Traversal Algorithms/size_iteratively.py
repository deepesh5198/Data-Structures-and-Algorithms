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


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)
root.right.left = Tree(31)
root.right.right = Tree(32)
root.left.left = Tree(40)
root.left.right = Tree(50)
root.left.left.left = Tree(60)
root.left.left.right = Tree(70)

def sizeIteratively(node):
    count = 0
    if not node:
        return
    else:
        q = Queue()
        q.enqueue(node)
        while not q.size == 0:
            node = q.dequeue()
            count +=1

            if node.left is not None:
                q.enqueue(node.left)

            if node.right is not None:
                q.enqueue(node.right)

    return count
print(sizeIteratively(root))
