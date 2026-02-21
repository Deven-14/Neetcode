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


# this can also be done using prefix_sums dict
# like the qustion for 1. Subarray sum equals k
