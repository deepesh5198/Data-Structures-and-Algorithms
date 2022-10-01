#problem 7. Check if a string is palindrome using Doubly ended queue

class Queue:
    def __init__(self):
        self.que = []
        self.size = 0

    def addfromrear(self, item):
        self.que.append(item)
        self.size +=1

    def addfromfront(self, item):
        self.que.insert(0,item)
        self.size +=1

    def removefromfront(self):
        if self.size <= 0:
            print("Queue Underflow!")

        else:
            item = self.que[0]
            self.que.remove(item)
            self.size -=1
            return item

    def removefromrear(self):
        if self.size <= 0:
            print("Queue Underflow!")

        else:
            item = self.que[-1]
            self.que.pop()
            self.size -=1
            return item

    def show_queue(self):
        print(self.que)


def checkPalindrome(test_string):
    Q = Queue()
    palindrome = False
    for char in test_string:
        Q.addfromrear(char)

    for _ in range(Q.size //2):
        if Q.removefromfront() == Q.removefromrear():
            palindrome = True
        else:
            palindrome = False
    return palindrome


print(checkPalindrome("madam"))