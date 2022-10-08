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
        newNode = Node(newdata)         #make a node object
        newNode.next = self.head        #point newNode's next to self.head
        self.head = newNode             #promote newNode to head
        self.length +=1                 #increment the length
        return

    def insert_at_end(self, newdata):
        """Inserts data at the end of the list same as Append"""
        newNode = Node(newdata)         #make node object with data

        #if list is empty, that is Head is None
        if self.head == None:           #if head is None
            newNode.next= self.head     #point newNode's next to self.head
            self.head = newNode         #make newNode as HEAD
            self.length +=1             #length + 1
            return
        #else traverse to the very last node and set its next as newNode
        else:
            current = self.head            #initialize current as head
            while current.next != None:    #check current.next is None, if its None the loop terminates
                current = current.next        #update current to next till current.next is not None

            current.next = newNode             #when current.next == None, current last.next as newNode
            self.length +=1                    #increment the length
            return

    def insert_at(self,pos,newdata):
        """Insert data at given position"""

        if pos > self.length or pos < -1:        #if pos is > listLength or < 0 : please insert valid pos
            print("Please insert valid position!")
        else:
            if pos == 0:                        #if pos = 0; call insert_at_beg()
                self.insert_at_beg(newdata)
                return

            elif pos == (self.length) or pos == -1:    #if pos = listLength; call insert_at_end()
                self.insert_at_end(newdata)
                return

            else:                               
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
                
    def insert_after(self, prev_node, data):
        if prev_node == None:
            print("This Node doesnt exist in List")
            return 
        else:
            newNode = Node(data)
            newNode.next = prev_node.next
            prev_node.next = newNode
            self.length +=1

            return    


    def delete_from_beg(self):           
        """Deletes element from beginning"""       
        if self.head is None:
            print("List is Empty")
            return

        else:
            temp = self.head                    #store the head HEAD in temp
            self.head = temp.next               #promote next node to HEAD
            del temp                            #delete temp

            self.length -= 1                        #decrease length by one
            return

    def delete_from_end(self):

        if self.head == None:
            print("List is Empty")       
            return

        if self.head.next is None:
            temp = self.head
            self.head = None                    #delete the head node
            
            del temp
            self.length - 1
            return

        else:
            current = self.head                 #begin from HEAD
            prev = None
            while current.next != None:            #traverse the list till last node
                prev = current                     #store second last node
                current = current.next             #store last node
            prev.next = None                    #make second last node as Last by setting its next None
            del current                            #delete last node

            self.length -=1
            return

    def delete_at(self,pos):
        if pos> self.length or pos<-1:                   #if pos > listLength or < 0 
            print("Please enter valid position")        #please enter valid position

        else:     
            if pos == 0:                        #if pos == 0; call delete_from_beg()
                self.delete_from_beg()
                return

            elif pos == self.length or pos == -1:   #if pos == listLength; call delete_from_end()
                self.delete_from_end()
                return
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
                return

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
list.insert_at_end(12)
list.insert_at_end(13)
list.insert_at_end(14)
list.insert_after(list.head, 39)
list.printlist()

