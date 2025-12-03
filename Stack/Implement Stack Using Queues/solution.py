from collections import deque
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        if len(self.queue1) == 1:
            return self.queue1.popleft()
        
        while len(self.queue2) > 1:
            self.queue1.append(self.queue2.popleft())
        
        return self.queue2.popleft()

    def top(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        if len(self.queue1) == 1:
            return self.queue1[0]
        
        while len(self.queue2) > 1:
            self.queue1.append(self.queue2.popleft())
        
        temp = self.queue2[0]
        self.queue1.append(self.queue2.popleft())
        return temp

    def empty(self) -> bool:
        return (not bool(self.queue1)) and (not bool(self.queue2))


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



from collections import deque
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        
    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



from collections import deque
class MyStack:

    def __init__(self):
        self.queue = None

    def push(self, x: int) -> None:
        self.queue = deque([x, self.queue]) 
        # prev = self.queue
        # self.queue = deque()
        # self.queue.append(x)
        # self.queue.append(prev)
        
    def pop(self) -> int:
        top = self.queue.popleft()
        self.queue = self.queue.popleft()
        return top

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not bool(self.queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()