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

#creating a list with Cycle by merging SLL and CLL

def mergeLlists(list1,list2):
    current = list1.head
    while current.next!=None:
        current = current.next
    current.next = list2.head

    return list1

mergeLlists(sll, cll)

def detect_cycle(merged_list):
    #initialize both slow and fast pointers as head
    slow_ptr = merged_list.head
    fast_ptr = merged_list.head

    #while fast pointer and slow pointer are not NONE
    while fast_ptr and slow_ptr:
        #move the fast pointer
        #slow pointer is still at head 
        fast_ptr = fast_ptr.next
        
        #return TRUE when fast pointer and slow pointer meet
        if fast_ptr == slow_ptr:
            print(slow_ptr.data)
            return True

        #if fast pointer reaches NONE return FALSE
        if fast_ptr == None:
            return False
        else:
            #move the fast pointer again
            fast_ptr = fast_ptr.next

        #check again if fast pointer met slow pointer
        if fast_ptr == slow_ptr:
            return True                     #return TRUE if pointers meet 
        else:
            #Now is the time to move slow pointer
            slow_ptr = slow_ptr.next
            
    return False
            
print(detect_cycle(sll))
# sll.printlist()