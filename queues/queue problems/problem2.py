#Implement queue using two stacks:
class StackQueue:
    def __init__(self):
        self.S1 = []
        self.S2 = []

    def enqueue(self, item):
        self.S1.append(item)

    def dequeue(self):
        for _ in range(len(self.S1)):
            top = self.S1.pop()
            self.S2.append(top)

        if len(self.S2) == 0:
            print("Queue Underflow!")
        else:    
            x = self.S2.pop()
            print(x, "was popped")
            del x

        for _ in range(len(self.S2)):
            self.S1.append(self.S2.pop())

    def printqueue(self):
        if len(self.S1) == 0 and len(self.S2) == 0:
            print("Queue is empty!")
        else:
            for i in self.S1:
                print(i)
        
    
q = StackQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()
q.dequeue()

q.printqueue()


