#Implementing queue using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LLQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0 

    def enqueue(self,data):
        newNode = Node(data)
        if self.front == None:
            newNode.next = self.rear
            self.front = self.rear = newNode
            self.length +=1
        else:
            temp = self.rear
            temp.next = newNode
            self.rear = newNode
            self.length +=1

    def dequeue(self):
        if self.rear == None or self.front == None:
            print("Queue is Empty!")

        else:
            temp = self.front
            self.front = self.rear = temp.next
            del temp
            self.length -= 1

    def printqueue(self):
        if self.front == None or self.rear == None:
            print("Queue Underflow!")

        else:
            current = self.front
            while current != self.rear:
                print(current.data)
                current = current.next
            print(current.data)

    def queue_rear(self):
        if self.rear == None:
            print("Queue is empty!")
        else:
            print(self.rear.data)

    def queue_front(self):
        if self.front == None:
            print("Queue is empty!")
        else:
            print(self.front.data)

    def queue_size(self):
        print(self.length)


q = LLQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.printqueue()
