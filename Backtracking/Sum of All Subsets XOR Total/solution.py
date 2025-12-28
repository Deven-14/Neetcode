class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets_total = 0
        n = len(nums)

        def backtracking(i, total):
            nonlocal subsets_total
            subsets_total += total

            for j in range(i, n):
                backtracking(j+1, total ^ nums[j])
            
        backtracking(0, 0)
        return subsets_total
    

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        def backtracking(i, total):
            if i == n:
                return total
            
            return backtracking(i+1, total ^ nums[i]) + backtracking(i + 1, total)
                        
        return backtracking(0, 0)
