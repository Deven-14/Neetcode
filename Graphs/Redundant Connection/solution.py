class DisjointSetUnion:

    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n
    
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

        if self.size[px] < self.size[py]:
            px, py = py, px
        self.size[px] += self.size[py]
        self.parents[py] = px
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) # coz if there are n nodes, then there should be n-1 edges
        # so if we take len(edges) then here coz of the extra edge, it'll be the no of nodes
        dsu = DisjointSetUnion(n+1) # n is number of nodes, but the nodes start from [1, n], so n+1
        
        for (x, y) in edges:
            if not dsu.union(x, y):
                return [x, y]


class DisjointSetUnion:

    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parents[x] == x:
            return x
        
        p = self.parents[x]
        if self.parents[p] != p: # checking it its parent is the root
            self.parents[x] = self.find(p)

        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False # already united, share the same parent, creats a cycle if we try to add again

        if self.size[px] < self.size[py]:
            px, py = py, px
        self.size[px] += self.size[py]
        self.parents[py] = px
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) # coz if there are n nodes, then there should be n-1 edges
        # so if we take len(edges) then here coz of the extra edge, it'll be the no of nodes
        dsu = DisjointSetUnion(n+1) # n is number of nodes, but the nodes start from [1, n], so n+1
        
        for (x, y) in edges:
            if not dsu.union(x, y):
                return [x, y]



class DisjointSetUnion:

    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n
    
    def find(self, x): # iterative approach
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False # already united, share the same parent, creats a cycle if we try to add again

        if self.size[px] < self.size[py]:
            px, py = py, px
        self.size[px] += self.size[py]
        self.parents[py] = px
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) # coz if there are n nodes, then there should be n-1 edges
        # so if we take len(edges) then here coz of the extra edge, it'll be the no of nodes
        dsu = DisjointSetUnion(n+1) # n is number of nodes, but the nodes start from [1, n], so n+1
        
        for (x, y) in edges:
            if not dsu.union(x, y):
                return [x, y]
        