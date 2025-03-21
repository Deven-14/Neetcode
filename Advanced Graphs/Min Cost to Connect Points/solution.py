class DisjointSetUnion:
    def __init__(self, nodes):
        self.rank = {node: 1 for node in nodes}
        self.parents = {node: node for node in nodes}
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.parents[py] = px
        self.rank[px] += self.rank[py]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        nodes = set(tuple(point) for point in points)
        dsu = DisjointSetUnion(nodes)
        n = len(points)

        # distances
        distances = []
        for i in range(n):
            point1 = tuple(points[i])

            for j in range(i+1, n):
                point2 = tuple(points[j])
                distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                distances.append((distance, point1, point2))

        distances.sort()

        min_cost = 0
        for distance, point1, point2 in distances:
            if dsu.union(point1, point2):
                min_cost += distance
        
        return min_cost

# * Kruskal's algorithm
# * disjoint set union
# * time complexity: O(n^2logn) or O(ElogE)
# * space complexity: O(n^2) or O(E), E ~ V^2 in worst case as each V can be connected to all other V = V * (V-1) ~ V^2


# * disjoint set union
# * here we could, pass the size (n) instead of nodes
# then use the idx of nodes as the key in rank and parents
# then use the idx of nodes as the point1, point2 in distances
# then use the idx of nodes as the key in dsu.union



from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            point1 = tuple(points[i])

            for j in range(i+1, n):
                point2 = tuple(points[j])
                distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                adj[point1].append((distance, point2))
                adj[point2].append((distance, point1))

        min_heap = [(0, tuple(points[0]))]
        min_cost = 0
        visited = set()

        while len(visited) < n:
            distance, point = heapq.heappop(min_heap)
            if point in visited:
                continue

            min_cost += distance
            visited.add(point)

            for (adj_distance, adj_point) in adj[point]:
                if adj_point in visited:
                    continue
                heapq.heappush(min_heap, (adj_distance, adj_point))
        
        return min_cost


# * Prim's algorithm
# * time complexity: O(n^2) or O(E)
# * space complexity: O(n^2) or O(E), E ~ V^2 in worst case as each V can be connected to all other V = V * (V-1) ~ V^2

