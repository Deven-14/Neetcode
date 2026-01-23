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
                
                

        