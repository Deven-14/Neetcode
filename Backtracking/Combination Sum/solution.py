class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []
        n = len(nums)
        nums.sort()

        def helper(i, combination_sum):
            if combination_sum == target:
                combinations.append(combination[:])
                return
            
            for j in range(i, n):
                total = combination_sum + nums[j]
                if total > target:
                    break
                combination.append(nums[j])
                helper(j, total)
                combination.pop()
            
        helper(0, 0)
        return combinations
            

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []
        n = len(nums)
        nums.sort()

        def dfs(i, combination_sum):
            if combination_sum == target:
                combinations.append(combination[:])
                return
            
            for j in range(i, n):
                total = combination_sum + nums[j]
                if total > target:
                    break
                combination.append(nums[j])
                dfs(j, total)
                combination.pop()
            
        dfs(0, 0)
        return combinations
            
    