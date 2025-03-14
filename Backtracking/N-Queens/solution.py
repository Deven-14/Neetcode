class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        def add_solution(positions):
            solution = []
            for i, j in enumerate(positions):
                row = ["."] * n
                row[j] = "Q"
                solution.append("".join(row))
            solutions.append(solution)
        
        def can_attack(curr_pos, positions):
            left_dia, right_dia = curr_pos-1, curr_pos+1
            for position in positions[::-1]:
                if curr_pos == position:
                    return True
                
                if left_dia >= 0 and left_dia == position:
                    return True
                
                if right_dia < n and right_dia == position:
                    return True
                
                left_dia -= 1
                right_dia += 1
                
            return False
        
        def backtrack(i, positions=[]):
            if i == n:
                add_solution(positions)
                return

            for j in range(n):
                if can_attack(j, positions):
                    continue
                positions.append(j)
                backtrack(i+1, positions)
                positions.pop()
        
        backtrack(0)
        return solutions
            
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        board = [["."] * n for _ in range(n)]
        cols = [False] * n
        left_dia = [False] * (2 * n - 1)
        right_dia = [False] * (2 * n - 1)
        mid_dia_idx = n - 1
        
        def backtrack(i):
            if i == n:
                solutions.append(["".join(row) for row in board])
                return

            for j in range(n):
                if cols[j] or right_dia[i + j] or left_dia[mid_dia_idx + i - j]:
                    continue
                board[i][j] = "Q"
                cols[j] = right_dia[i + j] = left_dia[mid_dia_idx + i - j] = True
                backtrack(i+1)
                cols[j] = right_dia[i + j] = left_dia[mid_dia_idx + i - j] = False
                board[i][j] = "."
        
        backtrack(0)
        return solutions
            
# * solution in leetcode
# * additionaly for i = 0, you can cut the n by 2 and iterate only for the first half of the columns
# * and then mirror the solution for the second half
# * this will reduce the number of solutions by half
# * but the time complexity will remain the same
# * as the time complexity is O(n!)
# * and the space complexity is O(n)
