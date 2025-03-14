class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        
        if len(stack) != numCourses:
            return []

        return stack[::-1]


# * TOPOLOGICAL SORT BFS
# * Time Complexity: O(V + E)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)] # Graph represented as an adjacency list

        for course, dependent_course in prerequisites:
            adj[course].append(dependent_course)
        
        def detect_cycle(course, visited, cycle, course_order): # dfs
            if course in cycle:
                return True
            
            if visited[course]:
                return False
            
            visited[course] = True
            cycle.add(course)
            for dependent_course in adj[course]:
                if detect_cycle(dependent_course, visited, cycle, course_order):
                    return True
            
            cycle.remove(course)
            course_order.append(course)
            
            return False
        
        visited = [False] * numCourses
        cycle = set()
        course_order = []
        for course in range(len(adj)):
            if detect_cycle(course, visited, cycle, course_order):
                return [] # indicating that the solution is not possible
        
        return course_order
    

# * cycle detection method using DFS
# * Time Complexity: O(V + E)


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        course_order = []
        visited = [False] * numCourses

        def dfs(course):
            if visited[course]:
                return
            
            course_order.append(course)
            visited[course] = True
            for dependent_course in adj[course]:
                indegrees[dependent_course] -= 1
                if indegrees[dependent_course] == 0:
                    dfs(dependent_course)
            
        for course, dependent_course in prerequisites:
            adj[course].append(dependent_course)
            indegrees[dependent_course] += 1

        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                dfs(course)
        
        if len(course_order) != numCourses:
            return []

        return course_order[::-1]


# * TOPOLOGICAL SORT DFS
# * Time Complexity: O(V + E)

