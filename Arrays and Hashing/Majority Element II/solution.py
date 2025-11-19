class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ele1 = ele2 = None
        count1 = count2 = 0

        for num in nums:
            if num == ele1:
                count1 += 1
            elif num == ele2:
                count2 += 1
            elif count1 == 0:
                ele1 = num
                count1 = 1
            elif count2 == 0:
                ele2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = count2 = 0
        for num in nums:
            if num == ele1:
                count1 += 1
            elif num == ele2:
                count2 += 1
        
        result = []
        m = n // 3
        if count1 > m:
            result.append(ele1)
        if count2 > m:
            result.append(ele2)
        
        return result
        