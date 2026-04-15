class MyCircularDeque(object):

    def __init__(self, k):
        self.size = k + 1
        self.deque = [0] * self.size
        self.front = 0
        self.rear = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.size
        self.deque[self.front] = value
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.size
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1) % self.size]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.size == self.front