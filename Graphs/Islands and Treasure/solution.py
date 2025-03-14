class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        INF = 2147483647

        def search_chests(i, j, visited):
            if i < 0 or i >= n or j < 0 or j >= m:
                return INF

            if visited[i][j] or grid[i][j] == -1:
                return INF

            if grid[i][j] == 0:
                return 0
            
            visited[i][j] = True
            
            paths = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            min_distance = INF
            for x, y in paths:
                distance = search_chests(x, y, visited)
                min_distance = min(min_distance, 1 + distance)
            
            visited[i][j] = False
            
            return min_distance
        
        # calculating distance
        for i in range(n):
            for j in range(m):
                if grid[i][j] == INF:
                    distance = search_chests(i, j, visited)
                    grid[i][j] = distance


# ! solution times out for large inputs
# * time complexity: O(n*m*4^(n*m))
# * space complexity: O(n*m)


from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        INF = 2147483647

        def bfs(i, j):
            visited = [[False] * m for _ in range(n)]
            queue = deque([(i, j)])
            visited[i][j] = True
            distance = 0

            while queue:
                curr_level_queue = queue
                queue = deque()

                while curr_level_queue:
                    i, j = curr_level_queue.popleft()
                    if grid[i][j] == 0:
                        return distance
                    
                    paths = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                    for x, y in paths:
                        if x < 0 or x >= n or y < 0 or y >= m:
                            continue
                        if visited[x][y] or grid[x][y] == -1:
                            continue
                        
                        queue.append((x, y))
                        visited[x][y] = True
                
                distance += 1
            
            return INF
        
        # calculating distance
        for i in range(n):
            for j in range(m):
                if grid[i][j] == INF:
                    distance = bfs(i, j)
                    grid[i][j] = distance


# * bfs solution works
# * time complexity: O(n*m) # O((n*m)^2)
# * space complexity: O(n*m)


from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        queue = deque()
        visited = [[False] * COLS for _ in range(ROWS)]

        # find chests
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = True
        
        # add land cells
        def add_land_cell(queue, i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return 
            if visited[i][j] or grid[i][j] == -1:
                return 
            queue.append((i, j))
            visited[i][j] = True
        
        # visit all chests and from chests go to each land cell with bfs
        # multi source bfs
        distance = 0
        while queue:
            curr_level_queue = queue
            queue = deque()

            while curr_level_queue:
                r, c = curr_level_queue.popleft()
                grid[r][c] = distance
                add_land_cell(queue, r + 1, c)
                add_land_cell(queue, r - 1, c)
                add_land_cell(queue, r, c + 1)
                add_land_cell(queue, r, c - 1)
            
            distance += 1

# * MULTI SOURCE BFS
# * time complexity: O(n*m)
# * space complexity: O(n*m)
