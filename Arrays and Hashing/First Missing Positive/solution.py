class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            
            j = i
            value = nums[j]
            while j >= 0 and j < n and (nums[j]-1) != j and 0 < value <= n:
                t = nums[value-1]
                nums[value-1] = value
                value = t
                j = value-1
            
            i += 1
        
        for i in range(n):
            if i != (nums[i]-1):
                return i+1
        
        return n+1



class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            v = nums[i]
            idx = v-1
            while 1 <= v <= n and nums[idx] != v:
                nums[idx], nums[i] = v, nums[idx]
                v = nums[i]
                idx = v - 1

        for i in range(n):
            if i != (nums[i]-1):
                return i+1
        
        return n+1

# In complete code inner loop will not run more than n time. In each iteration of inner loop we are placing one element at it correct position. So if inner loop run n times all element will get positioned at correct index. After that inner loop will not run any more
# So time complexity of first loop in worst case O(2*n)==O(n)
# https://leetcode.com/problems/first-missing-positive/solutions/4925619/hard-easy-positioning-elements-at-correc-nnic



class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        larger_num = n + 1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = larger_num

        for i in range(n):
            v = abs(nums[i])            
            if v <= n and nums[v-1] > 0: # if v is between [1, n] and is not visited nums[v-1] > 0
                nums[v-1] *= -1 # mark as visited

        for i in range(n):
            if nums[i] > 0:
                return i+1
        
        return n+1

# https://leetcode.com/problems/first-missing-positive/solutions/7362306/c-clear-and-efficient-solution-beats-100-osn0