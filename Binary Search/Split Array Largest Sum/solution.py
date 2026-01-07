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

