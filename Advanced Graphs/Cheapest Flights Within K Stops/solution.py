class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford's Algo
        infinity = float("inf")
        costs = [infinity] * n
        costs[src] = 0
        
        for _ in range(k + 1): # instead of V-1 times, we need only k+1 times in this case
            temp_costs = costs.copy()

            for from_loc, to_loc, cost in flights:
                if costs[from_loc] == infinity:
                    continue
                
                temp_costs[to_loc] = min(temp_costs[to_loc], costs[from_loc] + cost)
        
            costs = temp_costs # so that each iteration, only those many number of edges are considered

        return -1 if costs[dst] == infinity else costs[dst]



from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Shortest Path Fastest Algorithm
        adj = [[] for _ in range(n)]
        
        for (from_loc, to_loc, cost) in flights:
            adj[from_loc].append((cost, to_loc))
                
        # add the source node to the heapq
        stops = 0
        queue = deque([(0, src, stops)]) # src to src is 0
        costs = [float("inf")] * (n) # equavalent of distances
        costs[src] = 0

        while queue:
            cost, from_loc, stops = queue.popleft()
            if stops > k:
                continue

            for adj_cost, to_loc in adj[from_loc]:
                total_cost = cost + adj_cost

                if total_cost < costs[to_loc]:
                    costs[to_loc] = total_cost
                    queue.append((total_cost, to_loc, stops + 1))

        return costs[dst] if costs[dst] != float("inf") else -1

# * Shortest Path Faster Algorithm