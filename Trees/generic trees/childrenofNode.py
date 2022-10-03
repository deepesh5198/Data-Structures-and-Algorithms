#problem 44:given a node in a generic tree find the number of children of that node.
#solution: since, tree is represented as first_child/next_sibling method; for a given node in the tree,
#we just need to point it to its first_child and traverse all its next siblings:

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

def countChilrenOf(current):
    count = 0
    current = current.first_child

    while current:
        count +=1
        print(current.data)
        current = current.next_sibling

    return count


print("No. of children: ", countChilrenOf(root.first_child.next_sibling))