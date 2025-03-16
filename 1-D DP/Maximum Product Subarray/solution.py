class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = curr_max = prod_max = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]

            temp = max(num, num * curr_max, num * curr_min)
            curr_min = min(num, num * curr_max, num * curr_min)
            curr_max = temp

            prod_max = max(prod_max, curr_max)
        
        return prod_max


# * kandane's algorithm
# * Time Complexity: O(n)
# * Space Complexity: O(1)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = suffix = 0
        prod_max = nums[0]
        n = len(nums)

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            prod_max = max(prod_max, prefix, suffix)
        
        return prod_max


# * The subarray with the maximum product may be entirely in the prefix (left side) or in the suffix (right side).
# * If there is an odd number of negative values, the maximum product may be on either side of the first or last negative number.
# * The prefix-suffix approach handles zeros efficiently because:
# * When we encounter 0, prefix and suffix reset.
# * This allows the product calculation to restart without including a 0.