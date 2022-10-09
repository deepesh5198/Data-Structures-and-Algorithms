#Problem: given a LL of random numbers, rearrange list in such a way that all even numbers
# appear at beginning. 
#example: [1]-[2]-[3]-[4]-[5]-[6] -----> [6]-[4]-[2]-[1]-[3]-[5]

import re
from singly_linkedlist import SLinkedList

sll = SLinkedList()

sll.insert_at_end(8)
sll.insert_at_end(2)
sll.insert_at_end(6)
sll.insert_at_end(4)
sll.insert_at_end(12)
sll.insert_at_end(10)

# class Node:
#     def __init__(self, data = None):
#         self.data = data
#         self.next = None

def evenThenOdd(list):
    current = list.head
    count = 0
    while current.next != None:
        if current.data%2 == 0:
            temp = current.data
            list.delete_at(count)
            list.insert_at_beg(temp)
            count +=1
            current = current.next
        else:
            count = count+1
            current = current.next
    if current.data%2 == 0:
        temp = current.data
        list.delete_from_end()
        list.insert_at_beg(temp)

# evenThenOdd(sll)

def evenThenOdd_bysplit(list):
    result_list = SLinkedList()
    current = list.head
    while current.next != None:
        if current.data%2 == 0:
            result_list.insert_at_beg(current.data)
            current = current.next
        else:
            result_list.insert_at_end(current.data)
            current = current.next
    if current.data%2 == 0:
            result_list.insert_at_beg(current.data)
    else:
        result_list.insert_at_end(current.data)

    return result_list

evenodd = evenThenOdd_bysplit(sll)
evenodd.printlist()

# def eventhenOdd_efficient(list):
#     if list.head.data%2==0:
#         temp = list.head.data
#         list.head = list.head.next
#         list.insert_at_end(temp)
        
#     # dummyNode = Node(0)
#     # dummyNode.next = list.head
#     # list.head = dummyNode

#     #[1]-[2]-[3]-[4]-[5]-[6] -----> [6]-[4]-[2]-[1]-[3]-[5]

#     current = list.head
#     while current.next != None:

#         if current.data%2 == 0:
#             temp = current.data
#             prev.next = current.next
#             del current
#             list.insert_at_beg(temp)
#             current = prev.next

#         else:
#             prev = current
#             current = current.next


#     if current.data%2 == 0:
#         temp = current.data
#         list.insert_at_beg(temp)
#         list.delete_from_end()
    
# eventhenOdd_efficient(sll)
# sll.printlist()



