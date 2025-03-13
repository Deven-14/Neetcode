import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.max_heap = [-stone for stone in stones]
        heapq.heapify(self.max_heap)
        
        while len(self.max_heap) > 1:
            stone_y = - heapq.heappop(self.max_heap)
            stone_x = - heapq.heappop(self.max_heap)
            if stone_y == stone_x:
                continue
            
            stone_z = stone_y - stone_x
            heapq.heappush(self.max_heap, -stone_z)
        
        if self.max_heap:
            return - self.max_heap[0]
        
        return 0

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.max_heap = [-stone for stone in stones]
        heapq.heapify(self.max_heap)
        
        while len(self.max_heap) > 1:
            stone_y = - heapq.heappop(self.max_heap)
            stone_x = - heapq.heappop(self.max_heap)
            if stone_y > stone_x:
                heapq.heappush(self.max_heap, - (stone_y - stone_x))
        
        if self.max_heap:
            return - self.max_heap[0]
        
        return 0
        