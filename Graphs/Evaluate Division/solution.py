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
