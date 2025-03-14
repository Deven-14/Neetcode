class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(r, c, visited):
            if r < 0 or r == ROWS or c < 0 or c == COLS:
                return
            
            if visited[r][c] or board[r][c] == "X":
                return
            
            board[r][c] = "#"
            visited[r][c] = True

            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r, c - 1, visited)
        
        visited = [[False] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            dfs(r, 0, visited)
            dfs(r, COLS-1, visited)
        
        for c in range(COLS):
            dfs(0, c, visited)
            dfs(ROWS-1, c, visited)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"


# TODO: later do a BFS solution and a Union Find solution