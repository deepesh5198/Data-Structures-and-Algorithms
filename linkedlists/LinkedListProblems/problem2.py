# a code to implement singly linked list

class Node:
    def __init__(self, data):
        """Function to initialize node"""
        self.data = data    #defining data field of node
        self.next = None    #defining next as NULL

class SLinkedList:

    def __init__(self):
        """Initializing LinkedList"""
        self.head = None
        self.length = 0

    def insert_at_beg(self, newdata):
        """Insertion at beginning"""
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode
        self.length +=1

    def insert_at_end(self, newdata):
        """Inserts data at the end of the list same as Append"""
        newNode = Node(newdata)         #make node object with data
        
        #if list is empty, that is Head is None
        if self.head == None:           #if head is None
            self.head = newNode         #make newNode as HEAD

        #else traverse to the very last node and set its next as newNode
        else:
            last = self.head            #initialize last as head
            while last.next != None:    #check last.next is None, if its None break the loop
                last = last.next        #update last to next

        last.next = newNode             #when last.next == None, set last.next as newNode
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
            print("List is Empty")
        else:
            head = self.head                
            self.head = head.next               #promote next node to HEAD
            del head                            #delete previous HEAD

        self.length -= 1                        #decrease length by one

    def delete_from_end(self):
        last = self.head                        #begin from HEAD
        if last.next is None:
            self.head = None                    #delete the head node
            print("List is Empty")
            del last

        else:
            prev = None
            while last.next != None:            #traverse the list till last node
                prev = last                     #store second last node
                last = last.next                #store last node
            prev.next = None                    #make second last node as Last by setting its next None
            del last                            #delete last node

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

    def reverseit(self):
        #this method reverse the list
        if self.length ==0:
            print("Nothing to reverse!")

        elif self.length == 1:
            self.printlist()

        else:
            last = None
            current = self.head
            while current != None:
                nextNode = current.next
                current.next = last
                last = current
                current = nextNode
            self.head = last


    def listlength(self):
        """calculates the length of the linked list"""

        current = self.head             #set current node as HEAD
        count = 0                       #initialize count
        while current != None:          #run the loop till the current node is None
            count +=1
            current = current.next      #update current node to next node
        print("length of list:", count)                    #print the length

    def printlist(self):
        """prints the list"""
        if self.head == None:
            print("List is Empty")
        current = self.head             #set current node as HEAD
        while current != None:          #run the loop till the current node is None
            print(current.data)         #print the data in the node
            current = current.next      #update node to next node

list = SLinkedList()
list.insert_at_beg(23)
list.insert_at_beg(25)
list.insert_at_beg(36)
list.insert_at_beg(69)

list.printlist()
list.reverseit()
print("-"*80)
list.printlist()
