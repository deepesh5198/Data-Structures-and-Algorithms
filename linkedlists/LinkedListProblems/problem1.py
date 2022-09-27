#implement stack using linked list
#property of stack FILO
#operations: PUSH : insert at end
#            POP  : delete at end
#            TOP  : show top element

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.length +=1
            print("Pushed ", data)

        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode

            self.length +=1
            print("Pushed ", newNode.data)

    def pop(self):
        #remove the last element form the stack
        if self.head == None:
            print("Stack is Empty")

        elif self.length == 1:
            temp = self.head
            self.head = None
            print("Popped ", temp.data)
            del temp

        else:
            current= self.head
            prev = None
            while current.next !=None:
                prev = current
                current = current.next
            print("Popped ", current.data)
            del current
            prev.next = None
            self.length -=1

    def top(self):
        if self.head == None:
            print("Stack is Empty")

        else:
            current = self.head
            while current.next!=None:
                current = current.next
            print(current.data)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.pop()
stack.top()