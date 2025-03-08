class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack and self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0) # 0 
            self.min_val = val
        else:
            self.stack.append(val - self.min_val)
            if val < self.min_val:
                self.min_val = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val < 0:
            self.min_val = self.min_val - val # min_val - (actual_val - old_min_val) = actual_val - (actual_val - old_min_val)

    def top(self) -> int:
        val = self.stack[-1]
        if val > 0:
            return self.min_val + val
        else:
            return self.min_val

    def getMin(self) -> int:
        return self.min_val
