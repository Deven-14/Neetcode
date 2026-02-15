class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [-1] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        
        self.parents[py] = px
        self.size[px] += self.size[py]
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        critical = []
        pseudo_critical = []

        edges_with_idx = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
        edges_with_idx.sort()

        mst_edges = set()
        mst_weight = 0
        dsu = DisjointSetUnion(n)
        for w, u, v, i in edges_with_idx:
            if dsu.union(u, v):
                mst_edges.add(i)
                mst_weight += w
            if len(mst_edges) == n-1:
                break
        
        for i in mst_edges:
            dsu = DisjointSetUnion(n)
            tree_weight = 0
            tree_edges = 0

            for w, u, v, j in edges_with_idx:
                if i == j:
                    continue
                if dsu.union(u, v):
                    tree_edges += 1
                    tree_weight += w
                if tree_edges == n-1:
                    break

            if tree_edges != n-1 or tree_weight > mst_weight:
                critical.append(i)
            elif tree_weight == mst_weight:
                pseudo_critical.append(i)
        
        for i in set(list(range(len(edges)))) - mst_edges:
            dsu = DisjointSetUnion(n)
            u, v, w = edges[i]
            dsu.union(u, v)
            tree_weight = w
            tree_edges = 1

            for w, u, v, j in edges_with_idx:
                if dsu.union(u, v):
                    tree_edges += 1
                    tree_weight += w
                if tree_edges == n-1:
                    break

            if tree_weight == mst_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]

