class DisjointSetUnion:

    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [0] * n
        self._components = n
    
    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False # already united, share the same parent, creats a cycle if we try to add again

        self._components -= 1 # reducing one component as we are joining 2 components
        # joining separate components
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.size[px] += self.size[py]
        self.parents[py] = px
        return True
    
    def components(self):
        return self._components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DisjointSetUnion(n)

        for (x, y) in edges:
            dsu.union(x, y)
        
        return dsu.components()


# * this problem is made for union find
# * later try to implement using DFS and BFS