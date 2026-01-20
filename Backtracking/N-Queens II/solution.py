class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [False] * n
        left_dia = [False] * (2 * n - 1)
        right_dia = [False] * (2 * n - 1)
        mid_dia_idx = n - 1

        def backtracking(i):
            if i == n:
                return 1
            
            sub_solutions = 0
            for j in range(n):
                if cols[j] or right_dia[i + j] or left_dia[mid_dia_idx - i + j]:
                    continue
                cols[j] = right_dia[i + j] = left_dia[mid_dia_idx - i + j] = True
                sub_solutions += backtracking(i + 1)
                cols[j] = right_dia[i + j] = left_dia[mid_dia_idx - i + j] = False
            
            return sub_solutions
        
        solutions = 0
        i = 0
        for j in range(n // 2):
            cols[j] = right_dia[i + j] = left_dia[mid_dia_idx - i + j] = True
            solutions += 2 * backtracking(i + 1)
            cols[j] = right_dia[i + j] = left_dia[mid_dia_idx - i + j] = False
        
        if n % 2 == 1:
            j = (n // 2)
            cols[j] = right_dia[i + j] = left_dia[mid_dia_idx - i + j] = True
            solutions += backtracking(i + 1)
            cols[j] = right_dia[i + j] = left_dia[mid_dia_idx - i + j] = False
        
        return solutions
        


