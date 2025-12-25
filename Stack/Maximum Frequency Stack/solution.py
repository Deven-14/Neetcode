from collections import Counter

class FreqStack:

    def __init__(self):
        self.stack = []
        self.counts = Counter()

    def push(self, val: int) -> None:
        stack2 = []
        self.counts[val] += 1
        count = self.counts[val]

        while self.stack and count < self.stack[-1][0]:
            stack2.append(self.stack.pop())
        
        self.stack.append((count, val))

        while stack2:
            self.stack.append(stack2.pop())

    def pop(self) -> int:
        _, val = self.stack.pop()
        self.counts[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()



from collections import Counter

class FreqStack:

    def __init__(self):
        self.stack = [[]]
        self.counts = Counter()
        self.max_count = 0

    def push(self, val: int) -> None:
        self.counts[val] += 1

        self.max_count = max(self.max_count, self.counts[val])
        if len(self.stack) == self.max_count:
            self.stack.append([])
        
        self.stack[self.counts[val]].append(val)
        
    def pop(self) -> int:
        if not self.stack[self.max_count]:
            self.max_count -= 1
        
        val = self.stack[self.max_count].pop()
        self.counts[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()



from collections import Counter

class FreqStack:

    def __init__(self):
        self.stack = [[]]
        self.counts = Counter()

    def push(self, val: int) -> None:
        self.counts[val] += 1
        count = self.counts[val]

        if len(self.stack) == count:
            self.stack.append([])
        
        self.stack[self.counts[val]].append(val)
        
    def pop(self) -> int:
        val = self.stack[-1].pop()
        self.counts[val] -= 1

        if not self.stack[-1]:
            self.stack.pop()
        
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()