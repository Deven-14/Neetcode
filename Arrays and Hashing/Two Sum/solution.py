class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            if (rem := target - nums[i]) in visited:
                return [visited[rem], i]
            visited[nums[i]] = i
