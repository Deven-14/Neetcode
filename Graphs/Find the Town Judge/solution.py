from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(int)
        trusts = defaultdict(int)

        for ai, bi in trust:
            trusted[bi] += 1
            trusts[ai] += 1
        
        town_people = n-1
        maybe_judges = [bi for bi, trusted_by in trusted.items() if trusted_by == town_people]

        for maybe_judge in maybe_judges:
            if trusts[maybe_judge] == 0:
                return maybe_judge
        
        return -1
        

from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(int)
        trusts = defaultdict(int)

        for ai, bi in trust:
            trusted[bi] += 1
            trusts[ai] += 1
        
        town_people = n-1
        maybe_judges = (bi for bi, trusted_by in trusted.items() if trusted_by == town_people)

        for maybe_judge in maybe_judges:
            if trusts[maybe_judge] == 0:
                return maybe_judge
        
        return -1
        

from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # indegree and outdegree combined
        delta = defaultdict(int)

        for ai, bi in trust:
            delta[bi] += 1
            delta[ai] -= 1
        
        town_people = n-1
        maybe_judges = [bi for bi, combined in delta.items() if combined == town_people]
        
        return -1 if len(maybe_judges) == 0 else maybe_judges[0]
        
