# a code to implement singly linked list

class Node:
    def __init__(self, data):
        """Function to initialize node"""
        self.data = data    #defining data field of node
        self.next = None    #defining next as NULL

class CSLinkedList:

    def __init__(self):
        """Initializing LinkedList"""
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_beg(self, newdata):
        """Insertion at beginning"""
        newNode = Node(newdata)
        if self.head == None:
            self.head = self.tail = newNode
            self.head.next = self.tail
            self.tail.next = self.head
            self.length +=1
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head
            self.length +=1

    def insert_at_end(self, newdata):
        """Inserts data at the end of the list same as Append"""
        newNode = Node(newdata)         #make node object with data
        if self.head == None:
            self.head = self.tail = newNode
            self.head.next = self.tail
            self.tail.next = self.head
            self.length +=1

        else:                                
            self.tail.next = newNode
            newNode.next = self.head
            self.tail = newNode
            self.length +=1

    def insert_at(self,pos,newdata):
        """Insert data at given position"""

        if pos > self.length or pos < 0:        #if pos is > listLength or < 0 : please insert valid pos
            print("Please insert valid position!")
        else:
            if pos == 0:                        #if pos = 0; call insert_at_beg()
                self.insert_at_beg(newdata)
            elif pos == (self.length):          #if pos = listLength; call insert_at_end()
                self.insert_at_end(newdata)

            else:                               #else
                newNode = Node(newdata)         #create a new node
                count = 0                       #initialize count
                current = self.head             #start counting from HEAD
                while count < pos-1:            #keep counting till pos-1
                    count +=1
                    current = current.next

                #at count == pos-1
                newNode.next = current.next     #make current_node's next as newNode's next
                current.next = newNode          #make current_node's next as newNode
                self.length +=1                 #increament lenght by one


    def delete_from_beg(self):           
        """Deletes element from beginning"""       
        if self.head is None:
            print("Nothing to delete!")

        elif self.length == 1:
            head = self.head = self.tail
            self.head = None
            self.tail = None
            del head

            self.length -= 1

        else:
            head = self.head                
            self.head = head.next
            self.tail.next = self.head               #promote next node to HEAD
            del head                            #delete previous HEAD

            self.length -= 1                        #decrease length by one

    def delete_from_end(self):
        if self.length == 0:
            print("Nothing to delete")
        elif self.length == 1:
            temp = self.head = self.tail
            self.head = None
            self.tail = None
            del temp
            self.length -= 1
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
            
            prev.next = self.head
            self.tail = prev
            del current

            self.length -=1

    def delete_at(self,pos):
        if pos> self.length or pos<0:                   #if pos > listLength or < 0 
            print("Please enter valid position")        #please enter valid position

        else:     
            if pos == 0:                        #if pos == 0; call delete_from_beg()
                self.delete_from_beg()

            elif pos == self.length:            #if pos == listLength; call delete_from_end()
                self.delete_from_end()

            else:
            #delete at middle
                count = 0                       #initialize count
                current = self.head             #begin count from HEAD
                prev = None                     #prev node
                
                while count < pos:              #keep counting till pos             
                    count +=1                   
                    prev = current              #store current as prev
                    current = current.next      #store current's next as current
                    
                #at count == pos
                prev.next = current.next        #make current_node's next as prev_node's next
                del current                     #delete current node
                self.length -= 1                #decreament length by one

    def listlength(self):
        """calculates the length of the linked list"""
        print(self.length)

    def printlist(self):
        """prints the list"""
        if self.head == None:
            print("List is Empty!")
        else:
            current = self.head             #set current node as HEAD
            while current.next != self.head:          #run the loop till the current node is None
                print(current.data)         #print the data in the node
                current = current.next
            print(current.data)             #update node to next node

list = CSLinkedList()
list.insert_at_beg(23)
list.insert_at_beg(25)
list.insert_at_beg(36)
list.insert_at_end(69)
list.delete_from_end()
list.delete_from_end()
list.delete_from_end()
list.delete_from_end()
list.insert_at_end(4)
list.insert_at_end(5)
list.insert_at_beg(69)
list.insert_at_beg(40)
list.delete_from_end()
list.delete_from_beg()
list.insert_at(1,69)
list.insert_at(2,69)
list.insert_at(2,50)
list.delete_at(4)
list.delete_at(1)
list.printlist()
list.listlength()