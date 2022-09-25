# a code to implement singly linked list
###still in PROGRESS!###
class Node():
    def __init__(self) -> None:
        self.data = self.set_data()
        self.next = self.set_next()
        self.length = 0

    def set_data(self, data):           #method for setting data field of the Node
        self.data= data                 

    def get_data(self):                 #method for getting data field of the Node
        return self.data

    def set_next(self, next):           #method for setting next field of the Node
        self.next = next
    
    def get_next(self):                 #method for getting next field of the Node
        return self.next

    def has_next(self):                 #method to check if the field as next field
        return self.next != None        #true if node points to another node 

    def listlenght(self):
        current = self.head
        count = 0
        while current != None:
            count +=1
            current = current.get_next()
        
        return count
class SLinkedList():

    def __init__(self):
        pass

    def insert_at_beg(self, data):
        newNode = Node()
        newNode.set_data(data)

        if self.length == 0:
            self.head = newNode
            newNode.set_next(None)

        else:
            newNode.set_next(self.head)
            self.head = newNode
            self.length += 1

list = SLinkedList().insert_at_beg(12)
