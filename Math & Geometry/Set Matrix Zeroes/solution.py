class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # we could use a rows and cols set, but O(1) space so
        # We can use the topmost row and leftmost column of the matrix as boolean arrays by marking 0 instead of true. 
        # However, since they overlap at one cell, we use a single variable to track the top row separately. 
        # We then iterate through the matrix and mark zeros accordingly.
        is_top_row_zero = any(col == 0 for col in matrix[0])

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    print(i, j, matrix[i][j])

        # making rows zeros [1, rows]
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i][:] = [0] * len(matrix[i])
        
        # making cols zeros
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
        if is_top_row_zero:
            matrix[0][:] = [0] * len(matrix[0])
        
        