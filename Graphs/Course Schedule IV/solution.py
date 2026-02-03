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