class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        subset_total = total // k
        
        if total % k != 0 or max(nums) > subset_total:
            return False

        nums.sort(reverse=True) # pruning
        subsets = [0] * k
        n = len(nums)

        def backtracking(i):
            if i == n:
                return True
            
            num = nums[i]
            for j in range(k):
                if subsets[j] == subset_total or subsets[j] + num > subset_total:
                    continue
                
                subsets[j] += num
                if backtracking(i + 1):
                    return True
                subsets[j] -= num

                if subsets[j] == 0:
                    break
            
            return False
        
        return backtracking(0)
    