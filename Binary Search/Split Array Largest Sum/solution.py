class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = max(nums)
        r = sum(nums[:n - k + 1])

        max_r, curr_r = r, r
        for i in range(n - k + 1, n):
            curr_r += nums[i] - nums[i - n + k - 1]
            max_r = max(max_r, curr_r)
        
        r = max_r
        min_largest_sum = r

        def check_nums_split(largest_sum):
            split_count = 1
            curr_sum = 0

            for num in nums:
                curr_sum += num
                if curr_sum > largest_sum:
                    curr_sum = num
                    split_count += 1
            
            return split_count <= k

        while l <= r:
            largest_sum = l + (r - l) // 2

            if check_nums_split(largest_sum):
                min_largest_sum = largest_sum
                r = largest_sum - 1
            else:
                l = largest_sum + 1
        
        return min_largest_sum


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = max(nums)
        r = sum(nums)
        min_largest_sum = r

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def check_nums_split(largest_sum):
            split_count = 0
            i = 0

            while i < n and split_count <= k:

                l, r = i + 1, n
                while l <= r:
                    mid = l + (r - l) // 2
                    if prefix[mid] - prefix[i] <= largest_sum:
                        l = mid + 1
                    else:
                        r = mid - 1
                
                i = r
                split_count += 1
            
            return split_count <= k
            

        while l <= r:
            largest_sum = l + (r - l) // 2

            if check_nums_split(largest_sum):
                min_largest_sum = largest_sum
                r = largest_sum - 1
            else:
                l = largest_sum + 1
        
        return min_largest_sum



# * slower, just did to understand how to do it using recursion (dp top-down approach)
from functools import cache

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        inf = float("inf")

        @cache
        def dfs(i, m):
            if i == n:
                return 0 if m == 0 else inf
            if m == 0:
                return inf
            
            min_largest_sum = inf
            curr_sum = 0
            for j in range(i, n - m + 1):
                curr_sum += nums[j]
                min_largest_sum = min(min_largest_sum, max(curr_sum, dfs(j + 1, m - 1)))
            
            return min_largest_sum
        
        return dfs(0, k)


# TODO: dp bottom-up approach