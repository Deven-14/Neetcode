class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = None
        count = 0

        for num in nums:
            if num != ele:
                if count > 0:
                    count -= 1
                else:
                    count = 1
                    ele = num
            else:
                count += 1
        
        return ele