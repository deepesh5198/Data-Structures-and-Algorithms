class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)
root.right.left = Tree(35)
root.right.right = Tree(25)
root.right.left.left = Tree(78)
root.right.left.right = Tree(69)
root.right.right.left = Tree(33)
root.right.right.right = Tree(100)
root.left.right = Tree(40)
root.left.left = Tree(50)
root.left.left.left = Tree(60)
root.left.left.right = Tree(70)

def traverseZigZag(root):
    result = []
    currentlevel = []
    
    if not root:
        return 

    else:
        currentlevel.append(root)
        lefttoright = True
        while len(currentlevel) != 0:
            levelresult = []
            nextlevel = []
            while len(currentlevel) != 0:
                node = currentlevel.pop()
                levelresult.append(node.data)

                if lefttoright:
                    if node.left != None:
                        nextlevel.append(node.left)
                    if node.right != None:
                        nextlevel.append(node.right)

                else:
                    if node.right != None:
                        nextlevel.append(node.right)
                    if node.left != None:
                        nextlevel.append(node.left)
                    
            currentlevel = nextlevel
            lefttoright = not(lefttoright)
            result.append(levelresult)
        
    return result


print(traverseZigZag(root))


        