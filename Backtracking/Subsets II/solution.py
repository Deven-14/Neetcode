class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sub_sets = []
        nums.sort()
        subset = []
        
        def backtrack(i):
            if i == n:
                sub_sets.append(list(subset))
                return
            
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            while (i+1) < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0)
        return sub_sets


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sub_sets = [[]]
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            idx = n_prev_subsets if i > 0 and nums[i] == nums[i-1] else 0
            
            n_prev_subsets = len(sub_sets)
            for j in range(idx, len(sub_sets)):
                new_subset = list(sub_sets[j])
                new_subset.append(nums[i])
                sub_sets.append(new_subset)

        return sub_sets


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        subsets = []
        subset = []

        def backtrack(i):
            subsets.append(list(subset))

            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                subset.append(nums[j])
                backtrack(j+1)
                subset.pop()
            
        backtrack(0)
        return subsets