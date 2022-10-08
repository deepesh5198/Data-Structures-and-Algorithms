from singly_linkedlist import SLinkedList

sll = SLinkedList()

sll.insert_at_end(0)
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.insert_at_end(4)
sll.insert_at_end(5)

def reverse_in_pairs(list):
    if not list.head:
        return 

    def swap(node_a,node_b):
        """a utility function to swap two nodes"""
        temp = node_a.data
        node_a.data = node_b.data
        node_b.data = temp

    head = list.head

    while head != None and head.next != None:
        swap(head, head.next)
        head = head.next.next

    return list

listt = reverse_in_pairs(sll)

listt.printlist()
