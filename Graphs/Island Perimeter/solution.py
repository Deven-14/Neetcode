class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j, visited = set()):
            perimeter = 0
            visited.add((i, j))

            paths = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for k, l in paths:
                if (k, l) in visited:
                    continue
                elif not (0 <= k < ROWS and 0 <= l < COLS):
                    perimeter += 1
                elif grid[k][l] == 0:
                    perimeter += 1
                else:
                    perimeter += dfs(k, l)
            
            return perimeter
            

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return dfs(i, j)
        
        return 0
                
                

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j, visited = set()):
            if (i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == 0):
                return 1
            
            if (i, j) in visited:
                return 0

            visited.add((i, j))
            perimeter = dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
            
            return perimeter
            

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return dfs(i, j)
        
        return 0
                
                
