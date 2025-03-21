from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's Algorithm
        adj = defaultdict(list)

        for from_loc, to_loc in sorted(tickets, reverse=True):
            adj[from_loc].append(to_loc)
        
        stack = ["JFK"]
        res = []

        while stack:
            loc = stack[-1]

            if not adj[loc]:
                res.append(stack.pop())
            else:
                stack.append(adj[loc].pop())
        
        return res[::-1]

        

from collections import defaultdict
import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        
        tickets.sort()
        for (from_loc, to_loc) in tickets:
            adj[from_loc].append(to_loc)
        
        route = ["JFK"]
        def dfs(src_loc):
            if len(route) == len(tickets) + 1: # edges are the tickets, n vertices would have n-1 edges, ~ n edges would have n+1 vertices (repeated vertices)
                return True
            
            if src_loc not in adj: # no adj -> no outgoing from src loc
                return False
            
            adj_locs_copy = list(adj[src_loc]) # as we shouldn't manipulate while iterating
            for i, dest_loc in enumerate(adj_locs_copy):
                adj[src_loc].pop(i)
                route.append(dest_loc)

                if dfs(dest_loc):
                    return True
                
                route.pop()
                adj[src_loc].insert(i, dest_loc)
            
            return False
        
        dfs("JFK")
        return route

