class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search():
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2 # left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            
            return -1
        
        return binary_search()


import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        return idx if idx != len(nums) and nums[idx] == target else -1


# https://docs.python.org/3/library/bisect.html
# bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)