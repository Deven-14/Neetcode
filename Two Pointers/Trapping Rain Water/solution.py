class Solution:
    def trap(self, height: List[int]) -> int:
        total_area_of_water = 0
        n = len(height)

        max_height = 0
        prefix_max_height = [0] * n
        for i in range(n):
            max_height = max(max_height, height[i])
            prefix_max_height[i] = max_height
        
        max_height = 0
        suffix_max_height = [0] * n
        for i in range(n-1, -1, -1):
            max_height = max(max_height, height[i])
            suffix_max_height[i] = max_height
        
        for i in range(1, n-1):
            left_max_height = prefix_max_height[i]
            right_max_height = suffix_max_height[i]

            area_of_water = min(left_max_height, right_max_height) - height[i] # width = 1
            total_area_of_water += area_of_water
        
        return total_area_of_water

class Solution:
    def trap(self, height: List[int]) -> int:
        total_area_of_water = 0
        n = len(height)

        left, right = 0, n-1
        left_max, right_max = height[left], height[right]
        left += 1 # as water cannot be store in 0th idx
        right -= 1 # as water cannot be stored in n-1th idx

        while left <= right:
            if left_max < right_max:
                left_max = max(left_max, height[left]) # if we do this before cal. area then we don't need to check if area is negative, min it would be 0 coz of height[i]-height[i]
                total_area_of_water += left_max - height[left]
                left += 1 # next
            else:
                right_max = max(right_max, height[right])
                total_area_of_water += right_max - height[right]
                right -= 1
        
        return total_area_of_water

    # we don't need to compare with right because we are taking min, and left_max < right_max indicates that
