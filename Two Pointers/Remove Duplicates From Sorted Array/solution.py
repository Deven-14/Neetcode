class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 1
        n = len(nums)

        while j < n:
            if nums[j-1] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1
        
        return i