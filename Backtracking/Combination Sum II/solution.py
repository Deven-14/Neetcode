class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, combination_sum):
            if combination_sum == target:
                combinations.append(combination[:])
                return
            
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                total = combination_sum + candidates[j]
                if total > target:
                    break
                combination.append(candidates[j])
                dfs(j+1, total)
                combination.pop()
            
        dfs(0, 0)
        return combinations