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
root.left.left.left.left = Tree(88)

def maxDepthIterative(node):
    q = Queue()
    if not node:
        return 0

    else:
        q.enqueue([node,1])
        while q.size != 0:
            node, depth = q.dequeue()
            depth = max(0,depth)

            if node.left is not None:
                q.enqueue([node.left, depth+1])
            if node.right is not None:
                q.enqueue([node.right, depth+1])

        return depth

    
print(maxDepthIterative(root))

