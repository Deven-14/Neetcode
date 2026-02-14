from math import gcd

class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [-1] * n
        self.size = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        
        self.components -= 1
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parents[py] = px
        self.size[px] += self.size[py]


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        dsu = DisjointSetUnion(n)

        for i in range(n):
            for j in range(i+1, n):
                if gcd(nums[i], nums[j]) > 1:
                    dsu.union(i, j)
                    if dsu.components == 1:
                        return True
        
        return False
        
