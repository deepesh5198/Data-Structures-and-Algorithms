class GenericTree:
    def __init__(self,data):
        self.data = data
        self.first_child = None
        self.next_sibling = None


root = GenericTree(0)
root.first_child = GenericTree(1)
root.first_child.next_sibling = GenericTree(2)
root.first_child.next_sibling.next_sibling = GenericTree(3)
root.first_child.next_sibling.first_child = GenericTree(4)
root.first_child.next_sibling.next_sibling.next_sibling = GenericTree(5)
root.first_child.next_sibling.first_child.next_sibling = GenericTree(6)
root.first_child.next_sibling.first_child.next_sibling.next_sibling = GenericTree(7)


def countSiblings(current):
    count = 0
    while current:
        count += 1
        current = current.next_sibling
    return count

print("No. of siblings: ", countSiblings(root.first_child))
