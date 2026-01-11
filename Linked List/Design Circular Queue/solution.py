class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = -1
        self.rear = -1
        self.n = k

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.front = self.rear = 0
            self.queue[self.rear] = value
            return True
        
        if self.isFull():
            return False
        
        self.rear = (self.rear + 1) % self.n
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.front == self.rear:
            self.front = self.rear = -1
        
        else:
            self.front = (self.front + 1) % self.n

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.front]        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.rear == -1 and self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.n == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()