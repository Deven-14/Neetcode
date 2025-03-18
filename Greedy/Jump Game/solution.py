class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        last_idx = n-1

        while i < n:
            j = i + nums[i]

            if j >= last_idx:
                return True
            
            if i == j:
                return False

            max_idx = i + 1
            i = i + 2
            while i <= j:
                if (i + nums[i]) >= (max_idx + nums[max_idx]):
                    max_idx = i
                i += 1
            
            i = max_idx
        
        return False

