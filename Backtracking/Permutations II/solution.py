class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)
        perm = nums[:]

        def backtracking(i):
            if i == n:
                permutations.append(perm.copy())
                return
            
            num_set = set()
            for j in range(i, n):
                if perm[j] in num_set:
                    continue
                num_set.add(perm[j])
                perm[i], perm[j] = perm[j], perm[i]
                backtracking(i + 1)
                perm[i], perm[j] = perm[j], perm[i]
            
        backtracking(0)
        return permutations
    

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)
        nums.sort()
        perm = nums

        def backtracking(i):
            if i == n:
                permutations.append(perm.copy())
                return
            
            for j in range(i, n):
                if j > i and perm[i] == perm[j]:
                    continue
                perm[i], perm[j] = perm[j], perm[i]
                backtracking(i + 1)
            
            for j in range(n-1, i, -1):
                perm[i], perm[j] = perm[j], perm[i]
            
        backtracking(0)
        return permutations