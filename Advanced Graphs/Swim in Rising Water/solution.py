import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijkstra's algorithm - kinda

        min_heap = [(grid[0][0], (0, 0))]
        visited = set()
        t = grid[0][0]
        ROWS = len(grid)
        COLS = len(grid[0])
        min_elevations = {}

        while min_heap:
            elevation, pos = heapq.heappop(min_heap)
            if pos in visited:
                continue
            
            visited.add(pos)
            min_elevations[pos] = elevation

            x, y = pos
            for (r, c) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                    continue

                if (r, c) in visited:
                    continue
                
                heapq.heappush(min_heap, (max(grid[r][c], elevation), (r, c)))
        
        return min_elevations[(ROWS-1, COLS-1)]



# * efficient Dijkstra's algorithm

import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dijkstra's algorithm - kinda

        min_heap = [(grid[0][0], 0, 0)]
        t = grid[0][0]
        ROWS = len(grid)
        COLS = len(grid[0])
        min_elevations = [[float('inf')] * COLS for _ in range(ROWS)]
        min_elevations[0][0] = grid[0][0]

        while min_heap:
            curr_elevation, x, y = heapq.heappop(min_heap)
            if curr_elevation > min_elevations[x][y]:
                continue
            
            if (x, y) == (ROWS-1, COLS-1):
                return curr_elevation
            
            for (r, c) in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                    continue

                elevation = max(grid[r][c], curr_elevation)
                if elevation < min_elevations[r][c]:
                    min_elevations[r][c] = elevation
                    heapq.heappush(min_heap, (elevation, r, c))
        
        return min_elevations[(ROWS-1, COLS-1)]