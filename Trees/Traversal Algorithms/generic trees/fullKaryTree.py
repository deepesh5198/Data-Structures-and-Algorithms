# a full K-ary tree is a tree where each node either has 0 or K children
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

class BuildTree:
    def __init__(self,k, data = None):
        self.data = data
        self.childList = []


def buildfullKaryTree(A, k):
    n = len(A)
    if n<=0:
        return None
    indx = 0
    root = BuildTree(None, A[0])
    if not root:
        print("ERROR 5083: Memory Error!")
        return 

    Q = Queue()
    if Q == None:
        return None

    else:
        Q.enqueue(root)

    while Q.size != 0:
        temp = Q.dequeue()
        for i in range(k):
            indx += 1
            if indx < n:
                temp.childList.insert(i, BuildTree(None, A[indx]))
                Q.enqueue(temp.childList[i])

    return root

def preorderRec(kroot):
    if not kroot:
        return
    else:
        print(kroot.data)
        for node in kroot.childList:
            preorderRec(node)

A = [1,2,3,4,5,6,7,8,9,10,11,12,13]
kroot = buildfullKaryTree(A,3)
preorderRec(kroot)