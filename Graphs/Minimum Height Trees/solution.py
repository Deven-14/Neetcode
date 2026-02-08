
# ! TIME LIMIT EXCEEDED

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[float("inf")] * n for _ in range(n)]

        for x, y in edges:
            adj[x][y] = 1
            adj[y][x] = 1
        
        for mid in range(n):
            change = False
            for x in range(n):
                for y in range(n):
                    adj[x][y] = min(adj[x][y], 1 + max(adj[x][mid], adj[mid][y]))
        
        for x in range(n):
            adj[x][x] = 0

        heights = [max(heights) for heights in adj]
        min_height = min(heights)
        return [idx for idx, height in enumerate(heights) if height == min_height]


# ! TIME LIMIT EXCEEDED


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[float("inf")] * n for _ in range(n)]

        for x, y in edges:
            adj[x][y] = 1
            adj[y][x] = 1
        
        for mid in range(n):
            change = False
            
            for x in range(n):
                for y in range(n):
                    height = 1 + max(adj[x][mid], adj[mid][y])
                    if adj[x][y] >= height:
                        adj[x][y] = height
                        change = True
        
            if not change:
                break

        for x in range(n):
            adj[x][x] = 0

        heights = [max(heights) for heights in adj]
        min_height = min(heights)
        return [idx for idx, height in enumerate(heights) if height == min_height]



# * topological sort - with multi source BFS

from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        queue = []
        indegrees = [0] * n
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegrees[a] += 1
            indegrees[b] += 1
        
        for a, indegree in enumerate(indegrees):
            if indegree == 1:
                queue.append(a) # leaf nodes

        # instead of going inside to outside (from each node)
        # to identify the height
        # we go from outside to inside (multi source BFS)
        # to identify the heights for all nodes in one go

        while queue and n > 2:
            curr_level_queue = queue
            next_level_queue = deque()

            while curr_level_queue:
                node = curr_level_queue.pop()
                n -= 1
                for neighbour in adj[node]:
                    indegrees[neighbour] -= 1
                    if indegrees[neighbour] == 1:
                        next_level_queue.append(neighbour)
            
            queue = next_level_queue

        return list(queue)        

