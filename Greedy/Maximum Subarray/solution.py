class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kandane'a algo
        curr_max = nums[0]
        total_max = nums[0]
        for i in range(1, len(nums)):
            curr_max = max(curr_max + nums[i], nums[i])
            total_max = max(curr_max, total_max)
        
        return total_max


# * same answer using DP

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        
        return max(dp)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        
        return max(dp)