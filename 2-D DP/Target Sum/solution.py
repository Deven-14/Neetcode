from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def backtrack(i, total):
            if i == n and total == target:
                return 1
            
            if i == n:
                return 0
            
            return backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])
        
        return backtrack(0, 0)


from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def backtrack(i, total):
            if i == n:
                return int(total == target)
            
            return backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])
        
        return backtrack(0, 0)
    

# * without the @cache, the time complexity is O(2^n) and with the @cache, the time complexity is O(n*sum(nums))


