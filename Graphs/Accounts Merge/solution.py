from collections import defaultdict
from itertools import pairwise

class DisjointSetUnion:
    def __init__(self):
        self.parents = defaultdict(lambda: -1)
        self.size = defaultdict(int)
        
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
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.size[px] += self.size[py]
        self.parents[py] = px
    
    def components(self):
        disjoint_components = defaultdict(list)

        for ele in list(self.parents):
            disjoint_components[self.find(ele)].append(ele)
        
        return list(disjoint_components.values())


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name_to_dsu = defaultdict(DisjointSetUnion)
        merged_accounts = []

        for name, *emails in accounts:
            dsu = name_to_dsu[name]
            if len(emails) == 1:
                dsu.find(emails[0])
            for email1, email2 in pairwise(emails):
                dsu.union(email1, email2)
            
        for name, dsu in name_to_dsu.items():
            for disjoint_component in dsu.components():
                merged_accounts.append([name, *disjoint_component])
        
        return merged_accounts
