#problem 6: reverse first K elements in the queue 
# eg. [1,2,3,4,5,6,7,8,9,10], let k = 4, Output = [4,3,2,1,5,6,7,8,9,10]

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

class Stack:
    def __init__(self):
        self.stck = []
        self.size = 0
    def push(self, item):
        self.stck.append(item)
        self.size +=1
    def pop(self):
        if self.size <= 0:
            print("Queue Underflow!")

        else:
            item = self.stck[-1]
            self.stck.pop()
            self.size -=1

            return item

    


def reversefirstKelements(que, k):
    stack = Stack()                         #define an empty stack
    if que == None  or k > que.size:        # if queue is None or k > size of queue
        return 

    else:
        for _ in range(k):                  # till Kth element 
            stack.push(que.dequeue())       #dequeue till Kth element and push it to the stack
                                            #result = stack = [1,2,3,4]

        while stack.size != 0:              #empty the stack in queue
            que.enqueue(stack.pop())        #pop from Stack and enqueue to Queue
                                            #result = queue = [5,6,7,8,9,10,4,3,2,1]

        for _ in range(que.size - k):       #till size - kth element that is 10 - 4 = 6
            que.enqueue(que.dequeue())      #dequeue from Queue and enqueue to same Queue
                            
                                            #result = Queue = [4,3,2,1,5,6,7,8,9,10]
    return que              


queue = Queue()
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(14)
queue.enqueue(15)
queue.enqueue(16)
queue.enqueue(17)
queue.enqueue(18)
queue.enqueue(19)
queue.enqueue(20)

result = reversefirstKelements(queue, 2)
result.show_queue()