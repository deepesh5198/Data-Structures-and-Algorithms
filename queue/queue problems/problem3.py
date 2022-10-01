#implement stack using two Queues

#INCOMPLETE

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue == []:
            print("Queue underflow")

        else:
            item = self.queue[0]
            self.queue.remove(item)
            return item

    def size(self):
        return len(self.queue)

class Stack:
    def __init__(self):
        self.Q1 = Queue()
        self.Q2 = Queue()

    def push(self,item):
        if self.Q2.size() == 0:
            self.Q1.enqueue(item)
        else:
            self.Q2.enqueue(item)

    def pop(self):
        if self.Q2.size() == 0:
            while not (self.Q1.size() == 0):
                current = self.Q1.dequeue()
                if self.Q1.size() == 0:
                    return current
                else:
                    self.Q2.enqueue(current)

        else:
            while not (self.Q2.size() == 0):
                current = self.Q2.dequeue()
                if self.Q2.size() == 0:
                    return current
                    
                self.Q1.enqueue(current)

        print("Popped: ", current)

stck = Stack()
stck.push(2)
stck.push(3)
stck.pop()
stck.pop()