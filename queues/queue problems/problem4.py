#problem 4: given a queue of element divide it into 2 queues and then dequeue elements from each queue alternatively
#and store elements in a new queue

from itertools import pairwise


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
            
            
            
def isConsecutive(stk):
    que = Queue()
    pairwiseorder = 1

    #reverse the stack
    while not stk.size == 0:
        que.enqueue(stk.pop())        #pop the elements from stack and enqueue to queue till the stack is empty

    while not que.size == 0:
        stk.push(que.dequeue())       #dequeue elements from queue and push it to stack until the queue is empty

    while not stk.size == 0:          
        n = stk.pop()                 #take last element from stack and
        que.enqueue(n)                #enqueue to queue
        if not stk.size == 0:
            m = stk.pop()             #take second last element from stack   
            que.enqueue(m)            #and enqueue it to queue

            if (abs(n-m) != 1):       #check difference between last and 2nd last elements
                pairwiseorder = 0      # if difference != 1 then Pairwise order = 0
                break                   #break the operation

    while not que.size == 0:          #else:
        stk.push(que.dequeue())       #dequeue elements from the queue and push to stack again

    return pairwiseorder


stck = Stack()
stck.push(1)
stck.push(2)
stck.push(3)
stck.push(4)
stck.push(5)
stck.push(6)


print(isConsecutive(stk = stck))


