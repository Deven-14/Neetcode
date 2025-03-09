class Solution:
    def binary_search(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        start_idx = 0
        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid] <= nums[right]:
                start_idx = left
                break
            elif nums[left] <= nums[mid]: # 5, 6, 7, 8, 9, 1, 2
                left = mid + 1
            elif nums[mid] <= nums[right]: # 7, 8, 1, 2, 3, 4, 5, 6
                right = mid # it could be the smallest number
        
        if target <= nums[n-1]:
            idx = self.binary_search(nums, target, start_idx, n-1)
        else:
            idx = self.binary_search(nums, target, 0, start_idx-1)
        
        return idx
    

class Solution:
    def binary_search(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1
    
    def serach_min_ele(self, nums):
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid] <= nums[right]:
                return left
            elif nums[left] <= nums[mid]: # 5, 6, 7, 8, 9, 1, 2
                left = mid + 1
            elif nums[mid] <= nums[right]: # 7, 8, 1, 2, 3, 4, 5, 6
                right = mid # it could be the smallest number
    
    def search(self, nums: List[int], target: int) -> int:
        start_idx = self.serach_min_ele(nums)
        
        if target <= nums[-1]:
            idx = self.binary_search(nums, target, start_idx, len(nums)-1)
        else:
            idx = self.binary_search(nums, target, 0, start_idx-1)
        
        return idx
        