class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max, curr_min = 0, 0
        max_sum, min_sum = nums[0], nums[0]
        total = sum(nums)
        
        for num in nums:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
        
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
        # if all elements are negative
        # then total == min_sum, so t - min_sum = 0
        # max_sum will be the smallest neg num

# The maximum circular subarray sum falls into one of two cases: either the subarray does not wrap around, or it does. For the non-wrapping case, standard Kadane's algorithm finds the maximum subarray sum. For the wrapping case, if we remove a contiguous middle portion from the array, what remains is a prefix plus a suffix. Removing the minimum subarray sum leaves behind the maximum wrapping sum, which equals total - minSubarraySum. We take the better of these two cases, but if all elements are negative, the maximum is simply the largest single element.