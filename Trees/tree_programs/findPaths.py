#problem20: find all paths from root to each of the leaf nodes
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)
root.right.left = Tree(31)
root.right.right = Tree(32)
root.left.left = Tree(40)
root.left.right = Tree(50)


def pathAppender(root, path, paths):
    if not root:
        return 0
    else:
        path.append(root.data)
        paths.append(path)
        pathAppender(root.left, list(set(path+[root.data])), paths)
        pathAppender(root.right, list(set(path+[root.data])), paths)

def pathfinder(root):
    paths = []
    path = []
    pathAppender(root, path, paths)
    print("Paths: ", paths)


pathfinder(root)