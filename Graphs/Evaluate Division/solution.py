from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = defaultdict(dict)

        for (num, den), val in zip(equations, values):
            nodes[num][den] = val
            nodes[den][num] = 1 / val
        
        def dfs(num, den, visited):
            if num in visited:
                return -1

            dens = nodes[num]
            if den in dens:
                return dens[den]
            
            visited.add(num)
            for mid in dens:
                val = dfs(mid, den, visited)
                if val != -1:
                    return nodes[num][mid] * val
            
            return -1
        
        res = []
        for (num, den) in queries:
            if num not in nodes or den not in nodes:
                res.append(-1)
                continue
            res.append(dfs(num, den, set()))

        return res




from collections import defaultdict

class DisjointSetUnion:

    def __init__(self):
        self.parents = defaultdict(lambda: -1)
        self.weights = defaultdict(lambda: 1)
        # self.parent[x] = -1
        # self.weight[x] = 1.0
    
    def find(self, x):
        px = self.parents[x]
        if px == -1:
            return x # necessary to return x and not -1, it is it's own parent
        
        self.parents[x] = self.find(px)
        self.weights[x] *= self.weights[px]
        return self.parents[x]
        # x -> p -> root
        # x / root = (x / p) * (p / root)
        # weights[x] = x / root(x)
    
    def union(self, x, y, value):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return # already in union
        
        self.parents[rx] = ry
        self.weights[rx] = value * self.weights[y] / self.weights[x]

        # x / y = value

        # After calling find:
        # weight[x] = x / root_x
        # weight[y] = y / root_y

        # You attach -> Union:
        # root_x -> root_y
        # (root_x / root_y) = ?
        # so, parents[rx] = ry, because we do weights[x] = x / rootx
        # so if parent rx is ry then weights[rx] = rx / root(rx)=ry

        # x / y = value
            # x -> root_x -> root_y (new root)
            # (x / rx) * (rx / ry)
        # ((x / root_x) * (root_x / root_y)) / (y / root_y) = value
        # (weights[x] * (rx / ry)) / weights[y] = value 
        # root_x / root_y = value * (weight[y] / weight[x])
        # self.weight[root_x] = value * self.weight[y] / self.weight[x]
    
    def divide(self, x, y):
        # if parents of x and y are not same, there's no intermidiatory to divide
        if x not in self.parents or y not in self.parents or self.find(x) != self.find(y):
            return -1
        # same parent, so root is same 'root'
        return self.weights[x] / self.weights[y] 
        # (x / root) / (y / root) => (x / y * root / root) => (x/y)

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dsu = DisjointSetUnion()

        for (x, y), value in zip(equations, values):
            dsu.union(x, y, value)
        
        return [dsu.divide(x, y) for x, y in queries]




