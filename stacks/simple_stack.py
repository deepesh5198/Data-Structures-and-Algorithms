#Simple Implementation by using array (List)

class Stack:
    def __init__(self, limit=10):
        self.stck = []
        self.limit = limit

    def isempty(self):
        return len(self.stck)<=0

    def push(self, item):
        if len(self.stck) >= self.limit:
            print("stack overflow!")

        else:
            self.stck.append(item)
            print("pushed ", item)

    def pop(self):
        if len(self.stck) <= 0:
            print("stack underflow")

        else:
            print("popped ", self.stck[-1])
            return self.stck.pop()

    def peek(self):
        if len(self.stck)<=0:
            print("stack underflow!")

        else:
            self.stck[-1]

    def size(self):
        return len(self.stck)

stack = Stack(5)
print(stack.isempty())
stack.push(5)
stack.push("moon")
stack.push("car")
print(stack.size())
stack.pop()
print(stack.size())

                   