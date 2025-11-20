from itertools import accumulate
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = list(accumulate(nums, initial=0))

        count = sum(num == k for num in nums)

        n = len(nums)
        for i in range(2, n+1):
            for j in range(i, n+1):
                subarray_sum = prefix[j] - prefix[j-i]
                if subarray_sum == k:
                    count += 1
        
        return count
    
# ! time limit exceeded

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        curr_sum = 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            count += prefix_sums[diff]
            prefix_sums[curr_sum] += 1
        
        return count


