class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        comb = []
        nums = list(range(1, n+1))

        def helper(i, l):
            if l == k:
                combinations.append(list(comb))
                return
            
            for j in range(i, n):
                comb.append(nums[j])
                helper(j + 1, l + 1)
                comb.pop()
        
        helper(0, 0)
        return combinations

