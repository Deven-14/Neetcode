class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub_sets = [[]]
        
        for num in nums:
            new_subsets = []
            
            for subset in sub_sets:
                new_subset = list(subset)
                new_subset.append(num)
                new_subsets.append(new_subset)

            sub_sets.extend(new_subsets)
        
        return sub_sets


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub_sets = [[]]
        
        for num in nums:
            sub_sets += [ subset + [num] for subset in sub_sets]
        
        return sub_sets


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub_sets = []
        subset = []
        n = len(nums)

        def dfs(i):
            if i == n:
                sub_sets.append(list(subset))
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return sub_sets


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        subset = []

        def backtrack(i):
            subsets.append(list(subset))

            for j in range(i, n):
                subset.append(nums[j])
                backtrack(j+1)
                subset.pop()
            
        backtrack(0)
        return subsets

