class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_first_n = n * (n + 1) // 2
        return sum_of_first_n - sum(nums)
    

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        res = n
        for i in range(n):
            res ^= i ^ nums[i]
        
        return res

