from singly_linkedlist import SLinkedList

list1 = SLinkedList()
list2 = SLinkedList()

list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)
list1.insert_at_end(7)
list1.insert_at_end(9)
list1.insert_at_end(11)

list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)
list2.insert_at_end(8)
list2.insert_at_end(10)
list2.insert_at_end(12)


def merge_Ordered(list1 , list2):
    """this method merge two sorted LL into a new sorted LL"""
    #take head1 and head2
    head1 = list1.head
    head2 = list2.head

    #empty list: list3
    list3 = SLinkedList()

    #till head1 and head2 are not None
    while head1 and head2:

        #if head1.data < head2.data 
        if head1.data < head2.data:

            temp = head1.data
            # append head1.data to list3
            list3.insert_at_end(temp)

            #shift head1 to its next node
            head1 = head1.next


        #if head2.data < head1.data
        else:
            temp = head2.data
            #append head2.data to list3
            list3.insert_at_end(temp)

            #shift head2 to its next node
            head2 = head2.next
    if head1:
        list3.insert_at_end(head1.data)
    if head2:
        list3.insert_at_end(head2.data)


    return list3

list3 = merge_Ordered(list1, list2)
list3.printlist()

