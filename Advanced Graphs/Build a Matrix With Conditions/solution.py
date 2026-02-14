from collections import deque
class Solution:
    def bfs(self, k, conditions):
        n = k + 1
        adj = [[] for _ in range(n)]
        indegrees = [0] * n

        for a, b in conditions:
            adj[a].append(b)
            indegrees[b] += 1

        queue = deque([i for i in range(1, n) if indegrees[i] == 0])
        order = []

        while queue:
            i = queue.popleft()
            order.append(i)

            for j in adj[i]:
                indegrees[j] -= 1
                if indegrees[j] == 0:
                    queue.append(j)
        
        if len(order) < k:
            return None
        
        return order

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rorder = self.bfs(k, rowConditions)
        if not rorder:
            return []
        
        corder = self.bfs(k, colConditions)
        if not corder:
            return []
        corder = { key: i for i, key in enumerate(corder) }
        
        matrix = [[0] * k for _ in range(k)]
        for i, key in enumerate(rorder):
            matrix[i][corder[key]] = key
        
        return matrix


