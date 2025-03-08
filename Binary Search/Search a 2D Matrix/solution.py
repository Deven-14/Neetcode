class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search():
            left, right = 0, len(matrix[0]) - 1
            top, down = 0, len(matrix) - 1

            while left <= right and top <= down:
                l_r_mid = (left + right) // 2 # left + (right - left) // 2
                t_d_mid = (top + down) // 2

                if matrix[t_d_mid][right] < target:
                    top = t_d_mid + 1
                elif matrix[t_d_mid][left] > target:
                    down = t_d_mid - 1
                elif matrix[t_d_mid][l_r_mid] < target: # in middle row
                    left = l_r_mid + 1
                elif matrix[t_d_mid][l_r_mid] > target:
                    right = l_r_mid - 1
                else:
                    return True
            
            return False
        
        return binary_search()
    
    # we can separate the search into two binary searches
    # 1. search for the row
    # 2. search for the column


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search():
            left, right = 0, len(matrix[0]) - 1
            top, down = 0, len(matrix) - 1

            while top <= down:
                mid = (top + down) // 2
                if matrix[mid][right] < target:
                    top = mid + 1
                elif matrix[mid][left] > target:
                    down = mid - 1
                else:
                    break # in middle row
            
            if not top <= down:
                return False
            
            row = mid
            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] < target: 
                    left = mid + 1
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    return True
            
            return False
        
        return binary_search()


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows, ncols = len(matrix), len(matrix[0]) 

        l, r = 0, nrows * ncols - 1
        while l <= r:
            mid = l + (r - l) // 2
            row, col = mid // ncols, mid % ncols

            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                return True
        
        return False