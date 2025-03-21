class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1

        while left < right:
            if (total := numbers[left] + numbers[right]) > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left+1, right+1]
        
        