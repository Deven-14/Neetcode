class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        permutation = nums[:]
        n = len(nums)

        def backtrack(i):
            if i == n:
                permutations.append(list(permutation))
                return

            for j in range(i, n):
                permutation[i], permutation[j] = permutation[j], permutation[i]
                backtrack(i+1)
                permutation[i], permutation[j] = permutation[j], permutation[i]

        backtrack(0)
        return permutations