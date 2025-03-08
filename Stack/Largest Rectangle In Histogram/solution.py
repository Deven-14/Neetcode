class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        stack = []
        left_most = [0] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                left_most[i] = stack[-1] + 1 # stack[-1] is the idx where height > heights[i], so +1, next index on which height <= heights[i]
            
            stack.append(i)
        
        stack = []
        right_most = [n-1] * n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                right_most[i] = stack[-1] - 1
            
            stack.append(i)
        
        max_area = 0
        for i in range(n):
            left, right = left_most[i], right_most[i]
            max_area = max(max_area, heights[i] * (right_most[i] - left_most[i] + 1))
        
        return max_area


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = []

        for right in range(n):
            while stack and heights[stack[-1]] >= heights[right]:
                height = heights[stack.pop()]
                left = 0 if not stack else (stack[-1] + 1)
                max_area = max(max_area, height * (right - left))

            stack.append(right)

        right = n # or right + 1        
        while stack:
            height = heights[stack.pop()]
            left = (0 if not stack else (stack[-1] + 1))
            max_area = max(max_area, height * (right - left))
        
        return max_area

                            
