from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for course, dependent_course in prerequisites:
            adj[course].append(dependent_course)
            indegrees[dependent_course] += 1
        
        queue = deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)
        
        stack = []
        visited = [False] * numCourses
        while queue:
            course = queue.popleft()
            stack.append(course)
            visited[course] = True

            for dependent_course in adj[course]:
                if visited[dependent_course]:
                    continue
                
                indegrees[dependent_course] -= 1
                if indegrees[dependent_course] == 0:
                    queue.append(dependent_course)
        
        if len(stack) == numCourses:
            return True
        
        return False


# * cycle detection method using DFS

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)] # Graph represented as an adjacency list

        for course, dependent_course in prerequisites:
            adj[course].append(dependent_course)
        
        def detect_cycle(course, visited): # dfs
            if visited[course]:
                # cycles detected
                return True
            
            visited[course] = True
            for dependent_course in adj[course]:
                if detect_cycle(dependent_course, visited):
                    return True
            
            adj[course] = [] # we don't need to check it's dependents again when we visit it as dependent_course of another course
            visited[course] = False

            return False
        
        visited = [False] * numCourses
        for course in range(len(adj)):
            if detect_cycle(course, visited):
                return False # indicating that the solution is not possible
        
        return True



# * Khan's Algorithm doesn't require visited array
# * without visited array

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for course, dependent_course in prerequisites:
            adj[course].append(dependent_course)
            indegrees[dependent_course] += 1
        
        queue = deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)
        
        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1            
            for dependent_course in adj[course]:
                indegrees[dependent_course] -= 1
                if indegrees[dependent_course] == 0:
                    queue.append(dependent_course)
        
        return completed == numCourses
