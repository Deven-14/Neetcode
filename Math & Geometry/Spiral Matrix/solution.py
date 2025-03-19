class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
    
        spiral = []

        while top < bottom and left < right:
            
            spiral.extend(matrix[top][left : right])

            for i in range(top, bottom):
                spiral.append(matrix[i][right])

            spiral.extend(matrix[bottom][right : left : -1])

            for i in range(bottom, top, -1):
                spiral.append(matrix[i][left])
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        if top == bottom:
            spiral.extend(matrix[top][left : right + 1])
        elif left == right:
            for i in range(top, bottom + 1):
                spiral.append(matrix[i][left])

        return spiral

            