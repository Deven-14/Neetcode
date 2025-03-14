class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        
        def visit_island(i, j): # easy to do using stack too
            if i < 0 or i >= n or j < 0 or j >= m:
                return

            if visited[i][j] or grid[i][j] == "0":
                return
            
            visited[i][j] = True

            paths = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for x, y in paths:
                visit_island(x, y)
        
        n_islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    visit_island(i, j)
                    n_islands += 1
        
        return n_islands
