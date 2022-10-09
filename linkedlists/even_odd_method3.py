#Problem: given a LL of random numbers, rearrange list in such a way that all even numbers
# appear at beginning. 
#example: [1]-[2]-[3]-[4]-[5]-[6] -----> [6]-[4]-[2]-[1]-[3]-[5]
from singly_linkedlist import SLinkedList

sll = SLinkedList()

sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.insert_at_end(4)
sll.insert_at_end(5)
sll.insert_at_end(6)

def eventhenOdd_efficient(list):
    current = list.head
    while current != None and current.data%2==0:
        current = current.next

    if current == None:
        return

    #[1]-[2]-[3]-[4]-[5]-[6] -----> [6]-[4]-[2]-[1]-[3]-[5]
    while current.next != None:
        if current.data%2 == 0:

            temp = current.data
            prev.next = current.next
            del current
            list.insert_at_beg(temp)
            current = prev.next

        else:
            prev = current
            current = current.next


    if current.data%2 == 0:
        temp = current.data
        list.insert_at_beg(temp)
        list.delete_from_end()
    
eventhenOdd_efficient(sll)
sll.printlist()