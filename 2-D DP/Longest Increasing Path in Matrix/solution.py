from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        visited = [[False] * m for _ in range(n)]
        
        @cache
        def dfs(i, j):
            if i == n and j == m:
                return 0

            max_path = 1
            visited[i][j] = True

            # right
            if j+1 < m and matrix[i][j] < matrix[i][j+1]:
                max_path = max(max_path, 1 + dfs(i, j+1))
            
            # left
            if j-1 >= 0 and matrix[i][j] < matrix[i][j-1]:
                max_path = max(max_path, 1 + dfs(i, j-1))
            
            #top
            if i+1 < n and matrix[i][j] < matrix[i+1][j]:
                max_path = max(max_path, 1 + dfs(i+1, j))
            
            #down
            if i-1 >= 0 and matrix[i][j] < matrix[i-1][j]:
                max_path = max(max_path, 1 + dfs(i-1, j))
            
            return max_path
        
        max_path = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    max_path = max(max_path, dfs(i, j))
        
        return max_path
    
# * visited is not necessary, as the cache will take care of the visited cells


from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        @cache
        def dfs(i, j):
            if i == n and j == m:
                return 0

            max_path = 1

            # right
            if j+1 < m and matrix[i][j] < matrix[i][j+1]:
                max_path = max(max_path, 1 + dfs(i, j+1))
            
            # left
            if j-1 >= 0 and matrix[i][j] < matrix[i][j-1]:
                max_path = max(max_path, 1 + dfs(i, j-1))
            
            #top
            if i+1 < n and matrix[i][j] < matrix[i+1][j]:
                max_path = max(max_path, 1 + dfs(i+1, j))
            
            #down
            if i-1 >= 0 and matrix[i][j] < matrix[i-1][j]:
                max_path = max(max_path, 1 + dfs(i-1, j))
            
            return max_path
        
        max_path = 0
        for i in range(n):
            for j in range(m):
                max_path = max(max_path, dfs(i, j))
        
        return max_path
    

from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        @cache
        def dfs(i, j, prev_value):
            if i < 0 or i == n or j < 0 or j == m:
                return 0
            
            if matrix[i][j] <= prev_value:
                return 0

            max_path = 1
            max_path = max(max_path, 1 + dfs(i, j+1, matrix[i][j]))
            max_path = max(max_path, 1 + dfs(i, j-1, matrix[i][j]))
            max_path = max(max_path, 1 + dfs(i+1, j, matrix[i][j]))
            max_path = max(max_path, 1 + dfs(i-1, j, matrix[i][j]))
            
            return max_path
        
        max_path = 0
        for i in range(n):
            for j in range(m):
                max_path = max(max_path, dfs(i, j, float("-inf")))
        
        return max_path

# TODO: try to implement using kahn's algorithm, topological sort
# * take the indegree as the number of incoming edges from a lesser value to a greater value


