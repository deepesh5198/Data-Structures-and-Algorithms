#given a queue of integers rearrange the elements of the queue by interleaving the first half of the queue
#with the second half

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

def interLeavequeue(queue):
    Q1 = Queue()
    Q2 = Queue()
    queue_size = queue.size

    for _ in range(queue.size//2):
        Q1.enqueue(queue.dequeue())

    for _ in range(queue.size):
        Q2.enqueue(queue.dequeue())

    for _ in range(queue_size):
        while Q1.size != 0 and Q2.size != 0:
            queue.enqueue(Q1.dequeue())
            queue.enqueue(Q2.dequeue())

    return queue


que = Queue()
que.enqueue(11)
que.enqueue(12)
que.enqueue(13)
que.enqueue(14)
que.enqueue(15)
que.enqueue(16)
que.enqueue(17)
que.enqueue(18)
que.enqueue(19)
que.enqueue(20)
que.show_queue()
interleaved = interLeavequeue(que)
interleaved.show_queue()