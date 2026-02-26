from collections import deque
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        min_length = len(nums)
        window = deque()
        window_sum = 0

        for num in nums:
            window.append(num)
            window_sum += num

            while window_sum >= target:
                min_length = min(min_length, len(window))
                window_sum -= window.popleft()

        return min_length


# * this can also be done using prefix_sums dict
# * like the qustion for 1. Subarray sum equals k

from collections import deque
from bisect import bisect_left, bisect_right
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = 0
        prefix_sums = []
        for num in nums:
            prefix_sum += num
            prefix_sums.append(prefix_sum)
        
        if prefix_sums[-1] < target:
            return 0
        
        n = len(nums)
        j = bisect_left(prefix_sums, target)
        i = 0
        min_length = n

        while j < n:
            i = bisect_right(prefix_sums, prefix_sums[j] - target, lo=i, hi=j)
            min_length = min(min_length, j - i + 1)
            j += 1
        
        return min_length

    

from itertools import accumulate
from bisect import bisect_left, bisect_right
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sums = list(accumulate(nums))
        
        if prefix_sums[-1] < target:
            return 0
        
        n = len(nums)
        j = bisect_left(prefix_sums, target)
        i = 0
        min_length = n

        while j < n:
            i = bisect_right(prefix_sums, prefix_sums[j] - target, lo=i, hi=j)
            min_length = min(min_length, j - i + 1)
            j += 1
        
        return min_length

    

