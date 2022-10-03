#Problem: given a Simple Binary tree find the successor of the node
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Tree(1)
root.left = Tree(5)
root.right = Tree(11)
root.left.left = Tree(2)
root.right.left = Tree(16)
root.right.right = Tree(31)


def findInorderSuccessorOf(node):
    S = []
    if node != None:
        P = node
        S.append(P)
    if P.right != None:
        P = S.pop()
        P = P.left
        
    else:
        P = P.right
        while P.left != None:
            S.append(P)
        P = P.left
    return P

print(findInorderSuccessorOf(root.right))