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
            self.head = self.tail = newNode     #initially: HEAD == TAIL
            self.length +=1
            return

        else:
            newNode.next = self.head            
            self.head.prev = newNode
            self.head = newNode 
            self.length +=1
            return

    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            self.length +=1
            return

        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

            self.length +=1
            return

    def insert_at(self, pos, data):
        if pos > self.length or pos < -1:
            print("Please enter valid position.")
            return

        elif pos == 0:
            return self.insert_at_beg(data)

        elif pos == self.length or pos == -1:
            return self.insert_at_end(data)

        else:
            if pos <= self.length//2:
                newNode = Node(data)
                count = 0
                current = self.head
                
                while count < pos-1:
                    count+=1
                    current = current.next
                #pos = 3: [2]=[4]=[5]=[1*]=[7]
                #result = [2]=[4]=[5]=[newNode]=[1*]=[7]
                
                newNode.next = current.next
                current.next.prev = newNode
                current.next =newNode
                newNode.prev = current
                self.length +=1
                return
            
            else:
                count = self.length - 1
                current = self.tail
                newNode = Node(data)

                while count != pos:
                    count -=1
                    current = current.prev

                #pos = 3: [2]=[4]=[5]=[1*]=[7]
                #result = [2]=[4]=[5]=[newNode]=[1*c]=[7]
                newNode.prev = current.prev
                newNode.prev.next = newNode
                current.prev = newNode
                newNode.next = current
                self.length +=1
                return 
                
    def delete_at(self, pos):
        if pos > self.length or pos < -1:
            print("Please enter valid position.")

        elif pos == 0:
            return self.delete_from_beg()
            

        elif pos == self.length - 1 or pos == -1:
            return self.delete_from_end()
            
        elif pos <= self.length//2:
            """Deletes from front when item is close from head"""

            # print("this is first block")
            count = 0
            current = self.head
            previous = None
            #pos = 3: [2]=[4]=[5p]=[1*c]=[7]
            #result = [2]=[4]=[5p]=[7]
            while count < pos:
                count+=1
                previous = current
                current = current.next

            previous.next = current.next
            current.next.prev = previous
            del current

            self.length -=1
            return

        else:
            """Deletes from back when item is close from tail"""
            # print("this is 2nd block")
            count = self.length -1
            current = self.tail
            previous = None

            #pos = 3: [2]=[4]=[5p]=[1*c]=[7]
            #result = [2]=[4]=[5p]=[7]
            while count != pos:
                count -=1
                previous = current
                current = current.prev
            
            previous.prev = current.prev
            current.prev.next = previous
            del current
            self.length -=1

            return

    def delete_from_beg(self):
        if self.head == None:
            print("list is empty")
            return

        elif self.head.next == None:
            # del self.head
            temp = self.head
            self.head = None 
            self.tail = None
            
            del temp
            self.length -= 1
            return

        else:
            temp = self.head
            self.head = temp.next
            del temp
            # self.head.prev = None
            self.length -= 1
            return
            


    def delete_from_end(self):
        if self.length == 0:
            print("list is empty")
            return

        elif self.head.next == None:
            # del self.head
            temp = self.tail
            self.tail = None
            self.head = None
            del temp

            self.length -=1
            return

        else:
            temp = self.tail
            self.tail = temp.prev
            del temp
            # self.tail.next = None

            self.length -= 1
            return

    def printlist(self):
        if self.head == self.tail == None :
            print("List is Empty")
            return
        
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next
            return

        
list = DLinkedList()
list.insert_at_end(12)
list.insert_at_end(13)
list.insert_at_end(20)
list.insert_at_end(29)
list.insert_at_end(53)
list.insert_at_end(54)
list.insert_at_end(55)
list.insert_at_end(56)
list.insert_at_end(57)

list.delete_at(7)
# print(list.length)
list.printlist()

            