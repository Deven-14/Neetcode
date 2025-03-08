from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        max_nums = []

        for i in range(k):
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)
        
        max_nums.append(nums[window[0]])
        for i in range(k, len(nums)):
            if window[0] == (i-k):
                window.popleft()
            
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            
            window.append(i)
            max_nums.append(nums[window[0]])

        return max_nums

# Time complexity: O(n)
# Space complexity: O(k)

# with heap, O(nlogk)
# with deque, O(n)