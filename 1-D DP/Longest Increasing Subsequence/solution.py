from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def dfs(i, j):
            if i == n:
                return 0
            
            LIS = dfs(i+1, j) # skip element

            if j == -1 or nums[i] > nums[j]: # j == -1, if no smaller element exists
                LIS = max(LIS, 1 + dfs(i+1, i)) # i+1 -> next element, i -> smallest element
            
            return LIS
        
        return dfs(0, -1)


# * top-down DP with memoization


from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(n - 1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)
    
# * bottom-up DP with tabulation


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        long_sub_seq = [nums[0]]

        for i in range(1, len(nums)):
            num = nums[i]

            if num > long_sub_seq[-1]:
                long_sub_seq.append(num)
                continue

            j = len(long_sub_seq) - 1
            while j >= 0 and num <= long_sub_seq[j]:
                j -= 1
            
            long_sub_seq[j+1] = num
        
        return len(long_sub_seq)



from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        long_sub_seq = [nums[0]]

        for i in range(1, len(nums)):
            num = nums[i]

            if num > long_sub_seq[-1]:
                long_sub_seq.append(num)
                continue

            idx = bisect_left(long_sub_seq, num)
            long_sub_seq[idx] = num
        
        return len(long_sub_seq)