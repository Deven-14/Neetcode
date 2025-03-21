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