from circular_linkedlist import CSLinkedList
from singly_linkedlist import SLinkedList

sll = SLinkedList()
cll = CSLinkedList()
sll.insert_at_end(0)
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.insert_at_end(4)
sll.insert_at_end(5)

cll.insert_at_end(12)
cll.insert_at_end(13)
cll.insert_at_end(14)
cll.insert_at_end(24)
cll.insert_at_end(30)
cll.insert_at_end(35)

def merge_lists(list1, list2):
    """This method merges two lists of any kind
    
    We will use it to create a List with cycle"""

    current = list1.head
    while current.next != None:
        current = current.next
    current.next = list2.head

    return list1

#merging Singly Linked List with Circular Linked List    
merge_lists(sll, cll)

def start_of_Cycle(list):
    if list.head == None:
        return
    #slow pointer = list.head.next
    slow_ptr = list.head.next
    #fast pointer = list.head.next.next
    fast_ptr = slow_ptr.next

    #this code checks if list Terminates with None
    while slow_ptr != fast_ptr:
        slow_ptr = slow_ptr.next        
        try:
            fast_ptr = fast_ptr.next.next

        except AttributeError:
            print("No Cycle found")
            return
    #while loop stops when slow_ptr == fast_ptr

    #this code returns the node value where loop started.
    else:
        return slow_ptr.data

print(start_of_Cycle(sll))