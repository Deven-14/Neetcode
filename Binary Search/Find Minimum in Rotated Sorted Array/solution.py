class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid] <= nums[right]:
                return nums[left]
            elif nums[left] <= nums[mid]: # 5, 6, 7, 8, 9, 1, 2
                left = mid + 1
            elif nums[mid] <= nums[right]: # 7, 8, 1, 2, 3, 4, 5, 6
                right = mid # it could be the smallest number
            
            
            # else:
            #     return nums[right] # 9, 8, 7, 6, this case cannot happen

        
        