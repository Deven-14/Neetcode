class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        last_idx = n-1
        count = 0

        while i < last_idx:
            j = i + nums[i]
            count += 1

            if j >= last_idx:
                return count

            max_idx = i + 1
            i = i + 2
            while i <= j:
                if (i + nums[i]) >= (max_idx + nums[max_idx]):
                    max_idx = i
                i += 1
            
            i = max_idx
        
        return count

