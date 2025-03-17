from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        
        @cache
        def backtrack(i, j, k):
            if i == l1 and j == l2 and k == l3:
                return True
            
            if i < l1 and k < l3 and s1[i] == s3[k] and backtrack(i+1, j, k+1):
                return True
            
            if j < l2 and k < l3 and s2[j] == s3[k] and backtrack(i, j+1, k+1):
                return True
            
            return False
        
        return backtrack(0, 0, 0)


from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        
        @cache
        def backtrack(i, j):
            if i == l1 and j == l2:
                return True
            
            if i < l1 and s1[i] == s3[i+j] and backtrack(i+1, j):
                return True
            
            if j < l2 and s2[j] == s3[i+j] and backtrack(i, j+1):
                return True
            
            return False
        
        return backtrack(0, 0)

