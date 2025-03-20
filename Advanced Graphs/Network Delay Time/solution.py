import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        
        for (ui, vi, ti) in times:
            adj[ui].append((vi, ti))
        
        # Dijkstra's algo
        
        # add the source node to the heapq
        min_heap = [(k, 0)] # k to k is 0
        min_times = [float("inf")] * (n+1) # equavalent of distances
        min_times[k] = 0

        while min_heap:
            node, time = heapq.heappop(min_heap)

            for adj_node, adj_time in adj[node]:
                total_time = time + adj_time

                if total_time < min_times[adj_node]:
                    min_times[adj_node] = total_time
                    heapq.heappush(min_heap, (adj_node, total_time))
        
        min_time_required = max(min_times[1:]) # for all nodes to recieve
        # min for all nodes to receive will be max of min_times

        return min_time_required if min_time_required != float("inf") else -1


# ! one mistake above is min_heap should be a heap of (time, node) instead of (node, time)
# ! this is because we want to pop the node with the minimum time first

import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        
        for (ui, vi, ti) in times:
            adj[ui].append((vi, ti))
        
        # Dijkstra's algo
        
        # add the source node to the heapq
        min_heap = [(0, k)] # k to k is 0
        min_times = [float("inf")] * (n+1) # equavalent of distances
        visited = set()

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue

            visited.add(node)
            min_times[node] = time

            for adj_node, adj_time in adj[node]:
                if adj_node in visited:
                    continue
                total_time = time + adj_time
                heapq.heappush(min_heap, (total_time, adj_node))
        
        min_time_required = max(min_times[1:]) # for all nodes to recieve
        # min for all nodes to receive will be max of min_times

        return min_time_required if min_time_required != float("inf") else -1


# * time complexity: O((v + e)logv)
# O(V log V) for extracting nodes from the heap.
# O(E log V) for updating distances and pushing neighbors into the heap.


import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Bellman Ford Algorithm with early stopping
        min_times = [float("inf")] * (n + 1)
        min_times[k] = 0

        for _ in range(n - 1): # iterate atleast V-1 times
            updates = False

            for u, v, t in times: # iterate through all edges, sometimes, it could be using visiting all nodes with their outgoing edges
                if min_times[u] == float("inf"): # we don't know how to reach 'u' yet
                    continue
                
                if min_times[u] + t < min_times[v]:
                    min_times[v] = min_times[u] + t
                    updates = True
            
            if not updates:
                break
        
        min_time_required = max(min_times[1:]) # nodes [1, n]
        return min_time_required if min_time_required != float("inf") else -1


# * time complexity: O(V * E)
# * space complexity: O(V)


import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Bellman Ford Algorithm without early stopping
        min_times = [float("inf")] * (n + 1)
        min_times[k] = 0

        for _ in range(n - 1): # iterate atleast V-1 times
            for u, v, t in times: # iterate through all edges, sometimes, it could be using visiting all nodes with their outgoing edges
                if min_times[u] == float("inf"): # we don't know how to reach 'u' yet
                    continue
                
                if min_times[u] + t < min_times[v]:
                    min_times[v] = min_times[u] + t
        
        min_time_required = max(min_times[1:]) # nodes [1, n]
        return min_time_required if min_time_required != float("inf") else -1


# * time complexity: O(V * E)
# * space complexity: O(V)



import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Floyd Warshall Algorithm
        min_times = [[float("inf")] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            min_times[i][i] = 0
        
        for (u, v, t) in times:
            min_times[u][v] = t
        
        for mid in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    min_times[i][j] = min(min_times[i][j], min_times[i][mid] + min_times[mid][j])
        
        min_time_required = max(min_times[k][1:]) # [1:] coz starts from [1:n]
        return min_time_required if min_time_required != float("inf") else -1


# * time complexity: O(V^3)
# * space complexity: O(V^2)


# * Best solution is Dijkstra's algorithm with early stopping
# * time complexity: O((v + e)logv)