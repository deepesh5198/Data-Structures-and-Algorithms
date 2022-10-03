#problem: given a BST remove all the half nodes from it
#half node is one which only has one child
# NON RECURRSIVE METHOD

class Queue:
    def __init__(self):
        self.que = []
        self.size = 0

    def enqueue(self, item):
        self.que.append(item)
        self.size +=1

    def dequeue(self):
        if self.size <= 0:
            print("Queue Underflow!")

        else:
            item = self.que[0]
            self.que.remove(item)
            self.size -=1
            return item

    def show_queue(self):
        print(self.que)

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

#              10
#             /   \
#            7      15
#           / \    /  \
#          3   9  12   17
#                /  
#               11  

# in the given BST 12 is the Half Node remove its left or right node which makes it half node.

def removeHalfNodes(root):
    if not root:
        return 

    else:
        Q = Queue()
        Q.enqueue(root)
        temp = None

        while Q.size != 0:
            temp = Q.dequeue()

            if (temp.left == None and temp.right != None) or\
                (temp.left != None and temp.right == None):
                temp.left = temp.right = None

                return root

            else:
                if temp.left != None:
                    Q.enqueue(temp.left)
                
                if temp.right != None:
                    Q.enqueue(temp.right)        
    
tree_without_halfnodes = removeHalfNodes(root)

def traverseInorder(root):
    if not root:
        return
    else:
        traverseInorder(root.left)
        print(root.data)
        traverseInorder(root.right)

traverseInorder(tree_without_halfnodes)
