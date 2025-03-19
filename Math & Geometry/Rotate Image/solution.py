class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = m // 2

        for i in range(n):
            start = i
            end = m - 1 - i

            for j in range(end - start):
                top_left, top_right = matrix[i + j][i], matrix[i][end - j]
                bottom_left, bottom_right = matrix[end][i + j], matrix[end - j][end]

                matrix[i + j][i], matrix[i][end - j] = bottom_left, top_left
                matrix[end][i + j], matrix[end - j][end] = bottom_right, top_right
        


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = m // 2

        for i in range(n):
            start = i
            end = m - 1 - i

            for j in range(end - start):
                top_left, top_right = matrix[start + j][start], matrix[start][end - j]
                bottom_left, bottom_right = matrix[end][start + j], matrix[end - j][end]

                matrix[start + j][start], matrix[start][end - j] = bottom_left, top_left
                matrix[end][start + j], matrix[end - j][end] = bottom_right, top_right
        

# * REVERSE & TRANSPOSE METHOD
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        ROWS = len(matrix)
        COLS = len(matrix[0])
        for i in range(ROWS):
            for j in range(i, COLS):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]