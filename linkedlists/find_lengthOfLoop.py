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


def length_of_loop(list):
    if list.head == None:
        return

    else:
        slow_ptr = list.head.next
        fast_ptr = slow_ptr.next

        while fast_ptr != slow_ptr:
            slow_ptr = slow_ptr.next
            try:
                fast_ptr = fast_ptr.next.next
            except AttributeError:
                return

        current = slow_ptr
        length = 0
        while current.next != fast_ptr:
            length +=1
            current = current.next
        length = length+1

    return length

print(length_of_loop(sll))
        