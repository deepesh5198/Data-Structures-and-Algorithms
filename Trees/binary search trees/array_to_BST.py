class BSTNode:
    def __init__(self, data = None):
        self.data = data
        self.left  = None
        self.right = None

def array_to_BST(A, first_indx, last_indx):
    if A[first_indx] > A[last_indx]:
        return None

    else:
        newNode = BSTNode()
        if not newNode:
            print("Memory Error")
            return
        elif A[first_indx] == A[last_indx]:
            newNode.data = A[first_indx]
            newNode.left =  None
            newNode.right = None

        else:
            mid = first_indx + (last_indx - first_indx)//2
            newNode.data = A[mid]
            newNode.left = array_to_BST(A, first_indx, mid-1)
            newNode.right = array_to_BST(A, mid+1, last_indx)

        return newNode

A = [1,2,3,4,5,6,7]
root = array_to_BST(A, 0, len(A)-1)

result = []
def inorderTraverse(root):
    global result
    if not root:
        return
    else:
        inorderTraverse(root.left)
        result.append(root.data)
        inorderTraverse(root.right)
    return result


print(inorderTraverse(root))