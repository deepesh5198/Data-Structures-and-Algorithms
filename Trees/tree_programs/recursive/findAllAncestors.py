class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)
root.left.right = Tree(40)
root.left.left = Tree(50)
root.left.left.left = Tree(60)
root.left.left.right = Tree(70)


# def findAllAncestors(root, query_node
# ):
#     if not root:
#         return 0

#     else:
#         if (root.left.data == query_node
#          or root.right.data == query_node
#          or\
#              findAllAncestors(root.left, query_node
#              ) or findAllAncestors(root.right, query_node
#              )):
#              print(root.data)
#         return 1

# findAllAncestors(root, 70)

ancestors = []
# def findAllancestor(root, el):
#     if not root:
#         return
#     else:
#         global ancestors
#         if (root.left.data == el) or\
#             (root.right.data == el) or\
#             findAllancestor(root.left, el)or\
#             findAllancestor(root.right, el):
#             ancestors.append(root.data)
#     return ancestors



def findAllancestors(root,el):
    if not root:
        return False

    if root.data == el:
        return True

    if findAllancestors(root.left, el) or findAllancestors(root.right, el):
        ancestors.append(root.data)
        return ancestors

    return False

print(findAllancestors(root, 70))