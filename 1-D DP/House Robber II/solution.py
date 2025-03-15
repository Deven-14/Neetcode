class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        rob1, rob2 = 0, 0
        n = len(nums)

        for i in range(1, n):
            rob1, rob2 = rob2, max(rob2, nums[i] + rob1)
        
        max_rob = rob2
        rob1, rob2 = 0, 0
        for i in range(n-1):
            rob1, rob2 = rob2, max(rob2, nums[i] + rob1)
        
        return max(max_rob, rob2)