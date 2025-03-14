"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def dfs(node, nodes={}):
            if node.val in nodes:
                return nodes[node.val]
            
            new_node = Node(node.val)
            nodes[node.val] = new_node
            
            neighbors = []
            for neighbor in node.neighbors:
                new_neighbor = dfs(neighbor, nodes)
                neighbors.append(new_neighbor)
            
            new_node.neighbors = neighbors
            return new_node
        
        if not node:
            return None
        
        return dfs(node)

