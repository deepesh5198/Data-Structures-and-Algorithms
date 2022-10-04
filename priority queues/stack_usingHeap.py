class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0]*(self.maxsize+1)
        self.heap[0] = float("-inf")
        self.FRONT = 1

    def parent(self, indx):
        return indx//2

    def leftChild(self, indx):
        return 2*indx

    def rightChild(self, indx):
        return 2*indx+1

    def isLeaf(self, indx):
        if self.size//2 <= indx <= self.size:
            return True
        else:
            return False

    def swap(self, f_indx, s_indx):
        self.heap[f_indx], self.heap[s_indx] = (self.heap[s_indx], self.heap[f_indx])

    def minHeapify(self, indx):
        
        if not self.isLeaf(indx):
            if (self.heap[indx] > self.heap[self.leftChild(indx)]) or\
                (self.heap[indx] > self.heap[self.rightChild(indx)]):

                #swap with left child and heapify the left child
                if self.heap[self.leftChild(indx)] < self.heap[self.rightChild(indx)]:
                    self.swap(indx, self.leftChild(indx))
                    self.minHeapify(self.leftChild(indx))

                else:
                    self.swap(indx, self.rightChild(indx))
                    self.minHeapify(self.rightChild(indx))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        else:
            self.size +=1
            self.heap[self.size] = element

            current = self.size

            while self.heap[current] < self.heap[self.parent(current)]:
                self.swap(current, self.parent(current))
                current = self.parent(current)

    def print_heap(self):
        for i in range(1 , (self.size//2)+1):
            print("p: "+ str(self.heap[i]) +"\tlc: " + str(self.heap[2*i])+"\trc: " + str(self.heap[2*i+1]))

    def extractMin(self):
        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)

        return popped

    def findMin(minheap):
        min = float("inf")
        for i in range(minheap.size//2, minheap.size):
            if minheap.heap[i] < min:
                min = minheap.heap[i]

        return min

    def findMax(minheap):
        max = float("-inf")
        for i in range(minheap.size//2,minheap.size):
            if minheap.heap[i] > max:
                max = minheap.heap[i]

        return max


class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.PQ = MinHeap(self.maxsize)
    def push(self,item):
        self.PQ.insert(item)
        self.size +=1

    def pop(self):
        self.size -= 1
        return self.PQ.extractMax()

    def top(self):
        return self.PQ.findMax()

    def get_size(self):
        return self.size

    def isEmpty(self):
        if self.size <= 0:
            return True
        else:
            return False

stck = Stack(maxsize= 10)
stck.push(2)
stck.push(3)
stck.push(4)
