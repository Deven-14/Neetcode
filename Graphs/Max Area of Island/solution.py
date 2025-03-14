class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        
        def visit_island(i, j): # easy to do using stack too
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0

            if visited[i][j] or grid[i][j] == 0:
                return 0
            
            visited[i][j] = True

            paths = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            area = 1
            for x, y in paths:
                area += visit_island(x, y)
            
            return area
        
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = visit_island(i, j)
                    max_area = max(area, max_area)
        
        return max_area
