
# ! TIME LIMIT EXCEEDED

from functools import cache
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(i, j):
            if i == ROWS-1 and j == COLS-1:
                return 0
            
            visited[i][j] = True
            min_effort = float("inf")
            routes = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))

            for x, y in routes:
                if x < 0 or x >= ROWS or y < 0 or y >= COLS or visited[x][y]:
                    continue
                effort = max(abs(heights[i][j] - heights[x][y]), dfs(x, y))
                min_effort = min(min_effort, effort)
            
            visited[i][j] = False

            return min_effort

        return dfs(0, 0)


# ! TIME LIMIT EXCEEDED

import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        min_heap = [(0, 0, 0)]

        while min_heap:
            min_effort, i, j = heapq.heappop(min_heap)
            if i == ROWS-1 and j == COLS-1:
                return min_effort

            visited[i][j] = True
            routes = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))
            for x, y in routes:
                if x < 0 or x >= ROWS or y < 0 or y >= COLS or visited[x][y]:
                    continue
                new_min_effort = max(min_effort, abs(heights[i][j] - heights[x][y]))
                heapq.heappush(min_heap, (new_min_effort, x, y))

        return 0


# * Dijkstra's Algorithm

import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        min_heap = [(0, 0, 0)]

        while min_heap:
            min_effort, i, j = heapq.heappop(min_heap)
            if visited[i][j]: # VISITED in both the places is important
                continue

            if i == ROWS-1 and j == COLS-1:
                return min_effort

            visited[i][j] = True
            routes = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))
            for x, y in routes:
                if x < 0 or x >= ROWS or y < 0 or y >= COLS or visited[x][y]: # VISITED in both the places is important
                    continue
                new_min_effort = max(min_effort, abs(heights[i][j] - heights[x][y]))
                heapq.heappush(min_heap, (new_min_effort, x, y))

        return 0


# ! maximum recursion depth

import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        
        def dfs(i, j, limit, visited):
            if i == ROWS-1 and j == COLS-1:
                return True
            
            visited[i][j] = True
            routes = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))

            for x, y in routes:
                if x < 0 or x >= ROWS or y < 0 or y >= COLS or visited[x][y] or abs(heights[i][j] - heights[x][y]) > limit:
                    continue
                if dfs(x, y, limit, visited):
                    return True
            
            return False

        l, r = 0, max(max(row) for row in heights)
        min_effort = float("inf")
        
        while l <= r:
            mid = l + (r - l) // 2
            visited = [[False] * COLS for _ in range(ROWS)]
            if dfs(0, 0, mid, visited):
                min_effort = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return min_effort


# * slower than Dijkstra's Algorithm
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        
        def dfs_can_reach(limit):
            visited = [[False] * COLS for _ in range(ROWS)]
            stack = [(0, 0)]

            while stack:
                i, j = stack.pop()
                if i == ROWS-1 and j == COLS-1:
                    return True
            
                visited[i][j] = True
                routes = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))
                for x, y in routes:
                    if x < 0 or x >= ROWS or y < 0 or y >= COLS or visited[x][y] or abs(heights[i][j] - heights[x][y]) > limit:
                        continue
                    stack.append((x, y))
        
        
        l, r = 0, max(max(row) for row in heights)

        while l <= r:
            mid = l + (r - l) // 2
            if dfs_can_reach(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
        



class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [-1] * n # or list(rnage(n))
        self.size = [0] * n
    
    def find(self, x):
        if self.parents[x] == -1: # or == x
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        
        self.parents[py] = px
        self.size[px] += self.size[py]




class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # * Kruskal's Algorithm
        ROWS, COLS = len(heights), len(heights[0])

        edges = []
        for r in range(ROWS):
            for c in range(COLS):
                if r+1 < ROWS:
                    edges.append((
                        abs(heights[r][c] - heights[r + 1][c]),
                        r * COLS + c,
                        (r + 1) * COLS + c
                    ))
                if c+1 < COLS:
                    edges.append((
                        abs(heights[r][c] - heights[r][c+1]),
                        r * COLS + c,
                        r * COLS + c + 1
                    ))

        edges.sort()

        dsu = DisjointSetUnion(ROWS * COLS)
        start, end = 0, ROWS * COLS - 1
        for weight, u, v in edges:
            dsu.union(u, v)
            if dsu.find(start) == dsu.find(end):
                return weight
        
        return 0
        



from collections import deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # * SPFA - Shortest path faster algorithm
        ROWS, COLS = len(heights), len(heights[0])

        efforts = [[float('inf')] * COLS for _ in range(ROWS)]
        efforts[0][0] = 0

        queue = deque([(0, 0)])
        in_queue = [[False] * COLS for _ in range(ROWS)]
        in_queue[0][0] = True

        while queue:
            i, j = queue.popleft()
            in_queue[i][j] = False
            
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if x < 0 or x >= ROWS or y < 0 or y >= COLS:
                    continue
                
                effort = abs(heights[i][j] - heights[x][y])
                max_effort = max(efforts[i][j], effort)

                if max_effort < efforts[x][y]:
                    efforts[x][y] = max_effort

                    if not in_queue[x][y]:
                        queue.append((x, y))
                        in_queue[x][y] = True
            
        return efforts[ROWS-1][COLS-1]
