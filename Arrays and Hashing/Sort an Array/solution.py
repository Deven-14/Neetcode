class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        def partition(i, j):
            random_idx = (i + j) // 2
            p_idx = i
            nums[p_idx], nums[random_idx] = nums[random_idx], nums[p_idx]
            p = nums[p_idx]
            i += 1

            while nums[j] > p:
                j -= 1

            while i <= j and nums[i] <= p:
                i += 1
            
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

                while nums[i] <= p:
                    i += 1
                
                while nums[j] > p:
                    j -= 1
                
            nums[j], nums[p_idx] = nums[p_idx], nums[j]

            return j

        def quick_sort(i, j):
            if i >= j:
                return

            p_idx = partition(i, j)
            quick_sort(i, p_idx - 1)
            quick_sort(p_idx + 1, j)
        
        quick_sort(0, n-1)
        return nums