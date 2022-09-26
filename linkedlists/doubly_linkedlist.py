# code to implement doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_beg(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.length +=1

        else:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode 
            self.length +=1

    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.length +=1

        else:
            newNode.next = None
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

            self.length +=1

    def insert_at(self, pos, data):
        if pos > self.length or pos < 0:
            print("Please enter valid position.")

        elif pos == 0:
            self.insert_at_beg()

        elif pos == self.length:
            self.insert_at_end()
        else:
            newNode = Node(data)
            count = 0
            current = self.head
            
            while count < pos-1:
                count+=1
                current = current.next
            newNode.next = current.next
            current.next.prev = newNode
            current.next =newNode
            newNode.prev = current

            self.length +=1

    def delete_at(self, pos):
        if pos > self.length or pos < 0:
            print("Please enter valid position.")

        elif pos == 0:
            self.delete_from_beg()

        elif pos == self.length - 1 or pos == self.length:
            self.delete_from_end()
        else:
            # newNode = Node(data)
            count = 0
            current = self.head
            
            while count < pos:
                count+=1
                previous = current
                current = current.next
            previous.next = current.next
            current.next.prev = previous
            del current

            self.length -=1


    def delete_from_beg(self):
        if self.length == 0:
            print("list is empty")

        elif self.length == 1:
            # del self.head
            temp = self.head
            del temp
            self.head = self.tail = None
            self.length -= 1

        else:
            temp = self.head
            self.head = temp.next
            del temp
            # self.head.prev = None
            self.length -= 1


    def delete_from_end(self):
        if self.length == 0:
            print("list is empty")

        elif self.length == 1:
            # del self.head
            temp = self.tail
            del temp
            self.tail = self.head = None
            self.length -=1

        else:
            temp = self.tail
            self.tail = temp.prev
            del temp
            self.tail.next = None
            self.length -= 1

    def printlist(self):
        if self.head == self.tail == None :
            print("List is Empty")
        
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next
        
list = DLinkedList()
list.insert_at_beg(12)
list.insert_at_beg(13)
list.insert_at_beg(20)
list.insert_at_end(29)
list.insert_at_end(55)
list.insert_at(2,300)
list.insert_at(2,79)
list.insert_at(3,69)
list.delete_at(4)
list.delete_from_beg()
list.delete_from_beg()
list.delete_from_beg()
list.delete_from_beg()
list.delete_from_beg()
list.delete_from_beg()
list.delete_from_beg()
print(list.length)
list.printlist()

            