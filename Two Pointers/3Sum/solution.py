class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        sums = []

        def sub_two_sum(num, i):
            j, k = i+1, n-1
            while j < k:
                if (total := num + nums[j] + nums[k]) > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    sums.append([num, nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # remove repititions
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

        # for i = 0
        sub_two_sum(nums[0], 0)

        for i in range(1, n):
            if nums[i] > 0: # as it is sorted, if first one is > 0, sum can never be 0
                break
            
            if nums[i-1] == nums[i]:
                continue
            
            sub_two_sum(nums[i], i)
        
        return sums
        