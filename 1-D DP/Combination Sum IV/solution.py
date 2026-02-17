from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1 # 1 way for target = 0, select nothing

        for t in range(1, target + 1):
            for num in nums:
                if num > t:
                    break
                dp[t] += dp[t - num]

        return dp[target]

# * I came up with this solution by
# * first trying to solve the problem using recursion
# * when I was doing that I realized we are calculating
# * for every number from 1 to target, 
# * i.e., helper(t) with cache
# * when I saw we are calculating for every t
# * I thought about coin change problem
# * releated them and then solved this
# * one thing I did here was I kept the target as outside loop 
# * as from the start I want number of combinations for each t (smaller t)
# * then use that dp of comb of smaller t for bigger t