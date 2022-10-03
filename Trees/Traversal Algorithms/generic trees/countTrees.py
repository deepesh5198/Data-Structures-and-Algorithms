#problem: how many structurally unique BSTs are possible
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left  = None
        self.right = None

root = BSTNode(10)
root.left = BSTNode(7)
root.right = BSTNode(15)
root.left.left = BSTNode(3)
root.left.right = BSTNode(9)
root.right.left = BSTNode(12)
root.right.right = BSTNode(17)
root.right.left.left = BSTNode(11)
root.right.left.right = BSTNode(13)

#              10
#             /   \
#            7      15
#           / \    /  \
#          3   9  12   17
#                /  \
#               11  13

def countTrees(n):
    if n <= 1:
        return 1

    else:
        sum = 0
        for root in range(1, n+1):
            left = countTrees(root -1)
            right = countTrees(n - root)

            sum += left*right

    return sum

print(countTrees(10))