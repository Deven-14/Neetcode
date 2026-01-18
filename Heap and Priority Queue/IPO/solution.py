import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_heap = [(cap, profit) for cap, profit in zip(capital, profits)]
        max_heap = []
        heapq.heapify(min_heap)

        while k:

            while min_heap and min_heap[0][0] <= w:
                cap, profit = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -profit)
            
            if not max_heap:
                break
            
            profit = -heapq.heappop(max_heap)
            w += profit
            k -= 1
        
        return w


import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(capital)
        indices = list(range(n))
        indices.sort(key=lambda i: capital[i])
        i = 0
        max_heap = []

        while k:

            while i < n and capital[indices[i]] <= w:
                heapq.heappush(max_heap, -profits[indices[i]])
                i += 1
            
            if not max_heap:
                break
            
            profit = -heapq.heappop(max_heap)
            w += profit
            k -= 1
        
        return w

