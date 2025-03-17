from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum1 = sum2 = 0
        n = len(nums)

        @cache
        def partition(i, sum1, sum2):
            if i == n:
                return sum1 == sum2
            
            return partition(i+1, sum1 + nums[i], sum2) or partition(i+1, sum1, sum2 + nums[i])
        
        return partition(0, 0, 0)


from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: # odd
            return False
        
        sum1 = sum2 = 0
        n = len(nums)

        @cache
        def partition(i, sum1, sum2):
            if i == n:
                return sum1 == sum2
            
            return partition(i+1, sum1 + nums[i], sum2) or partition(i+1, sum1, sum2 + nums[i])
        
        return partition(0, 0, 0)


from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: # odd
            return False
        
        sum1 = sum2 = 0
        n = len(nums)

        half = total // 2

        @cache
        def partition(i, target):
            if i == n:
                return target == 0
            
            if target < 0:
                return False
            
            return partition(i+1, target) or partition(i+1, target - nums[i])
        
        return partition(0, half)


# TODO: add bottom-up DP solution