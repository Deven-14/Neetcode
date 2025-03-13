class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        def check_backtrack(i, j, idx, visited=set()):
            if idx == len(word):
                return True
            
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            
            if (i, j) in visited:
                return False

            if word[idx] != board[i][j]:
                return False
            
            visited.add((i, j))
            
            paths = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for (x, y) in paths:
                if check_backtrack(x, y, idx+1, visited):
                    return True
            
            visited.remove((i, j))
            
            return False
        
        for i in range(n):
            for j in range(m):
                if check_backtrack(i, j, 0):
                    return True
        
        return False
