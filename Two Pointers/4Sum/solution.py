class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        quadruplets = []
        
        def twoSumRemaining(first, second, start):
            i, j = start, n-1
            initial = first + second

            while i < j:
                if (total := initial + nums[i] + nums[j]) > target:
                    j -= 1
                elif total < target:
                    i += 1
                else:
                    quadruplets.append([first, second, nums[i], nums[j]])
                    i += 1
                    j -= 1
                
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
        
        for i in range(n):
            if nums[i] > target:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            first = nums[i]
            for j in range(i + 1, n):
                if first + nums[j] > target:
                    break
                
                if j > (i + 1) and nums[j] == nums[j-1]:
                    continue
                
                twoSumRemaining(first, nums[j], j+1)
        
        return quadruplets
