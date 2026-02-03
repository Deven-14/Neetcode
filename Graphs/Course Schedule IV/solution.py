
# * dfs
from functools import cache
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[a].add(b)
        
        @cache
        def dfs(a, b):
            if b in adj[a]:
                return True

            for dependent in adj[a]:
                if dfs(dependent, b):
                    return True
            
            return False
        
        return [dfs(a, b) for a, b in queries]


# * Topological sort
from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]
        indegrees = [0] * numCourses
        pre_reqs = [set() for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[a].add(b)
            indegrees[b] += 1
        
        queue = deque(i for i, indegree in enumerate(indegrees) if indegree == 0)
        
        while queue:
            node = queue.popleft()
            
            for dependent in adj[node]:
                pre_reqs[dependent].add(node)
                pre_reqs[dependent].update(pre_reqs[node])
                
                indegrees[dependent] -= 1
                if indegrees[dependent] == 0:
                    queue.append(dependent)
        
        return [u in pre_reqs[v] for u, v in queries]



# * Floyd Warshall Algorithm
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[False] * numCourses for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[a][b] = True
                
        for mid in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    adj[i][j] = adj[i][j] or (adj[i][mid] and adj[mid][j])
        
        return [adj[u][v] for u, v in queries]

