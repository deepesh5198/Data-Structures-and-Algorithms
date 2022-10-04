#Array representation of heap
#implementing maxheap

class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.heap = [0]*(self.maxsize+1)
        self.heap[0] = float("inf")
        self.FRONT  = 1
        self.size = 0

    def parent(self, indx):
        return indx//2

    def leftChild(self,indx):
        return 2*indx

    def rightChild(self, indx):
        return 2*indx + 1

    def isLeaf(self, indx):
        if self.size//2 <= indx <= self.size:
            return True
        else: 
            return False

    def swap(self, f_indx, s_indx):
        self.heap[f_indx], self.heap[s_indx] = (self.heap[s_indx], self.heap[f_indx])
    
    #Function to Heapify the node/element
    def maxHeapify(self, indx):
        #if node is non-leaf and smaller
        if not self.isLeaf(indx):
            if self.heap[indx] < self.heap[self.leftChild(indx)] or\
                self.heap[indx] < self.heap[self.rightChild(indx)]:
                
                #swap with left child if leftChild > rightChild
                if self.heap[self.leftChild(indx)] > self.heap[self.rightChild(indx)]:
                    self.swap(indx, self.leftChild(indx))
                    self.maxHeapify(self.leftChild(indx))

                #else, swap with right child
                else:
                    self.swap(indx, self.rightChild(indx))
                    self.maxHeapify(self.rightChild(indx))

    #function to insert a newnode into Maxheap
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        else:
            self.size += 1
            self.heap[self.size] = element

            current = self.size

            while (self.heap[current] > self.heap[self.parent(current)]):
                self.swap(current, self.parent(current))
                current = self.parent(current)


    def print_heap(self):
        for i in range(1, (self.size // 2)+1):
            print("p: "+str(self.heap[i]) + "\tlc: "+str(self.heap[2*i]) + "\trc: "+str(self.heap[2*i + 1]))


    def extractMax(self):
 
        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
         
        return popped

    def findMin(self):
        min = float("inf")
        for i in range(self.size//2, self.size):
            if self.heap[i] < min:
                min = self.heap[i]

        return min
 

     
maxHeap = MaxHeap(20)
maxHeap.insert(5)
maxHeap.insert(3)
maxHeap.insert(17)
maxHeap.insert(10)
maxHeap.insert(84)
maxHeap.insert(19)
maxHeap.insert(6)
maxHeap.insert(22)
maxHeap.insert(9)



# maxHeap.insert(8)
maxHeap.print_heap()
