import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        k -= 1
        while k:
            heapq.heappop(max_heap)
            k -= 1
        
        return -heapq.heappop(max_heap)
    
# time complexity: O(nlogn)
# space complexity: O(n)

import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num < pivot:
                    left.append(num)
                elif num > pivot:
                    right.append(num)
                else:
                    mid.append(num)
                
            if len(right) >= k:
                return quick_select(right, k)
            
            if len(mid) + len(right) < k:
                return quick_select(left, k - len(mid) - len(right))
            
            return pivot # in mid which means equal to pivot
        
        return quick_select(nums, k)


# time complexity: O(n) on average, O(n^2) in worst case
# space complexity: O(n)