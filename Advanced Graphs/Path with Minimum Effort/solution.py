
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
        