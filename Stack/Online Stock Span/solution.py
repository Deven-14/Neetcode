class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1

        while self.stack and price >= self.stack[-1][0]:
            top_price, top_count = self.stack.pop()
            count += top_count

        self.stack.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)