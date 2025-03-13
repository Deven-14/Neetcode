import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        heapq.heapify(self.min_heap)

        self.k = k
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
                
    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]

