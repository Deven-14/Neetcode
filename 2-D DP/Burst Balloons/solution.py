from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        @cache
        def dfs(nums):
            if len(nums) == 1:
                return nums[0]
            
            max_coins = 0
            for i, num in enumerate(nums):
                left = 1 if (i - 1) < 0 else nums[i - 1]
                center = num
                right = 1 if (i + 1) >= len(nums) else nums[i + 1]
                coins = left * center * right + dfs(tuple(nums[:i] + nums[i+1:]))
                max_coins = max(max_coins, coins)

            return max_coins
    
        return dfs(tuple(nums))


from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        @cache
        def dfs(nums):
            if len(nums) == 2: # [1, 1]
                return 0
            
            max_coins = 0
            for i in range(1, len(nums) - 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]
                coins += dfs(tuple(nums[:i] + nums[i+1:]))
                max_coins = max(max_coins, coins)

            return max_coins
    
        return dfs(tuple([1] + nums + [1]))


# * another approach is, instead of assuming we are poping the ith element first, let's assume we are poping the ith element last
# * so, then the sub arrays will be nums[:i] and nums[i+1:],
# * but if we are considering that the ith element is popped last, then the left and right sub arrays will never intersect
# * so, we can run it recursively for the left and the right sub array
# * but one key point to remember is that, the left and right sub arrays should also include the ith element at the end and begining respectively implicitely for calculation but doesn't pop them explicitly
# * similar to how we assume [1, ... 1] at the begining and the end and we don't pop them explicitly
# * so the left and the right sub problems would be [l, i-1] and [i+1, r] respectively, but we include the ith left and right elements implicitely during calculation


from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        @cache
        def dfs(l, r):
            if l > r:
                return 0
            
            max_coins = 0
            for i in range(l, r + 1): # including the right idx
                coins = dfs(l, i - 1) + dfs(i + 1, r)
                coins += nums[l - 1] * nums[i] * nums[r + 1] # popping ith element last, so considering the implicit l-1, r+1 elements present at the end, could be [1, 1] in the main sub array
                max_coins = max(max_coins, coins)

            return max_coins
    
        nums = [1] + nums + [1]
        return dfs(1, len(nums) - 2) 
        # we use the left and the right ones for calculation
        # but when we pass the values for l, r, we say 1, n-2, coz they don't come in the sub problem
        # they are there as helpers implicitely, on the left and the right end
        # similar when we assume consider to pop the ith element at the end,
        # the ith element will be present in left and right sub array implicitely for calculations
        # the left and the right sub array will never intersect or interate with reach other for calculations as we consider the ith element to be poped at the end
