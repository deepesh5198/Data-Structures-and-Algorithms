#Implementing stack using dynamic array
#a.k.a repeated doubling method, If the stack gets full create an array of
#double the size and copy the old elements in new array

class Stack:
    def __init__(self, limit = 1):
        self.stck = []
        self.limit = limit
        
    def isempty(self):
        return len(self.stck) <= 0

    def resize(self):
        newstck = list(self.stck)
        self.limit = 2*self.limit
        self.stck = newstck

    def push(self, item):
        if len(self.stck)>=self.limit:
            self.resize()
        self.stck.append(item)
        print("pushed ", item)

    def pop(self):
        if len(self.stck)<= 0:
            print("stack underflow")

        else: 
            print("popped ", self.stck[-1])
            return self.stck.pop()
            
    def peek(self):
        if len(self.stck) <=0:
            print("stack is empty")

        else:
            print(self.stck[-1])

    def size(self):
        print(len(self.stck))

stack = Stack()
stack.push(12)
stack.push(14)
stack.push(15)
stack.size()
stack.pop()
stack.size()

# a = 5*[None]
# print(a)