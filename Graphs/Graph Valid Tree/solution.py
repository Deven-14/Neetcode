class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        visited = {}
        cycle = set()

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
            visited[node1] = False
            visited[node2] = False
        
        def detect_cycle(node, parent_node):
            if node in cycle:
                return True
            
            if visited[node]:
                return False
            
            visited[node] = True
            cycle.add(node)

            for dependent_node in adj[node]:
                if dependent_node == parent_node:
                    continue

                if detect_cycle(dependent_node, node):
                    return True
            
            cycle.remove(node)
            return False
        
        if edges and detect_cycle(edges[0][0], None):
            return False # indicating not a tree
        
        return all(visited.values()) # checks if disjoint trees

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n-1): # for a tree with n nodes, there are n-1 edges
            return False

        adj = [[] for _ in range(n)]
        visited = set()

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        def detect_cycle(node, parent_node):
            if node in visited:
                return True
            
            visited.add(node)
            for dependent_node in adj[node]:
                if dependent_node == parent_node:
                    continue

                if detect_cycle(dependent_node, node):
                    return True
            
            return False
        
        if detect_cycle(0, None):
            return False # indicating not a tree
        
        return len(visited) == n # checks if disjoint trees

# TODO: later on, try to implement BFS and the union-find algorithm to solve this problem