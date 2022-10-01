#Implementing queue using Array

from matplotlib.widgets import EllipseSelector


class Queue(object):
    def __init__(self,limit = 5):
        self.queue =[]
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isQueueEmpty(self):
        return self.size <= 0

    def enqueue(self, item):
        if self.size >= self.limit:
            print("Queue Overflow!")
            return

        else: 
            self.queue.append(item)

        if self.front == None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size +=1

        print("Queue after Enqueue: ",self.queue)

    def dequeue(self):
        if self.size <= 0:
            print("Queue Underflow!")
            return 0

        else:
            self.queue.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None

            else:
                self.rear = self.size - 1

            print("Queue after Dequeue: ", self.queue)

    def get_rear(self):
        if self.rear == None:
            print("Queue is empty!")
            raise IndexError

        else:
            return self.queue[self.rear]
    
    def get_front(self):
        if self.front == None:
            print("Queue is empty!")
            raise IndexError
        else:
            self.queue[self.front]
        
    def queue_size(self):
        print(self.size)
        return self.size

que = Queue()
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.enqueue(6)
que.enqueue(69)
que.enqueue(54)

que.dequeue()
que.enqueue(54)
que.queue_size()
print(que.get_rear())
print(que.get_front())
            