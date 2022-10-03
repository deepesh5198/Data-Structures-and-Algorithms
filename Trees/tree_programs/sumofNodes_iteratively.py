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

root1 = Tree(1)
root1.left = Tree(2)
root1.right = Tree(3)
root1.right.left = Tree(4)
root1.right.right = Tree(5)
root1.left.left = Tree(6)
root1.left.right = Tree(7)
root1.left.left.left = Tree(8)
root1.left.left.right = Tree(9)
root1.left.left.left.left = Tree(10)

def sumofAllNodesinTree(root):
    q = Queue()
    q.enqueue(root)
    sum = 0
    if not root:
        return 0

    else:
        while q.size !=0:
            node = q.dequeue()
            sum += node.data

            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
            
    return sum
    
print(sumofAllNodesinTree(root1))