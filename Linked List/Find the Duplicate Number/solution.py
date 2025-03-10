class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # detecting cycle
        i, j = nums[0], nums[nums[0]] # important as i == j if initially assigned to i=0, j=0
        while i != j:
            i = nums[i]
            j = nums[nums[j]]
        
        # A = C principle of Floyd's Tortoise and Hare algorithm
        i = 0
        while nums[i] != nums[j]:
            i = nums[i]
            j = nums[j]
        
        return nums[i]
        