# Implementation of dynamic queue using array

from xml.etree.ElementInclude import LimitedRecursiveIncludeError

from matplotlib.widgets import EllipseSelector
from numpy import size


class DyQueue:
    def __init__(self, limit = 5):
        self.queue = limit*[]
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
    def isEmpty(self):
        return self.size <= 0

    def resize(self):
        newQue = self.queue
        self.limit = 2*self.limit
        self.queue = newQue

    def enqueue(self, item):
        if self.size >= self.limit:
            self.resize()

        else:
            self.queue.append(item)
        if self.front == None:
            self.front = self.rear = 0

        else:
            self.rear = self.size

        self.size += 1
        print("Queue after enqueue: ", self.queue)

    def dequeue(self):
        if self.size <= 0:
            print("Queue Underflow!")

        else:
            self.queue.pop(0)
            self.size -=1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1

            print("Queue after dequeue: ", self.queue)

    def get_rear(self):
        if self.rear == None:
            print("Queue is Empty!")
            raise IndexError

        else:
            print(self.queue[self.rear])

    def get_front(self):
        if self.front == None:
            print("Queue is Empty!")
            raise IndexError

        else:
            print(self.queue[self.front])

    def queue_size(self):
        return self.size

queue = DyQueue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(1)
queue.enqueue(2)

queue.get_front()
queue.get_rear()