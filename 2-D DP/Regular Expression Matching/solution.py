from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        
        @cache
        def backtrack(i, j):
            if i == n and j == m:
                return True
            
            if i < n and j == m:
                return False
            
            if i == n and j < m:
                return False
            
            print(i, s[i], j, p[j])
            if j + 1 < m and p[j+1] == "*":
                if (s[i] == p[j] or p[j] == "."):
                    if backtrack(i+1, j):
                        return True
                    else:
                        return backtrack(i, j+2) or backtrack(i+1, j+2)
                else: # not equal
                    return backtrack(i, j+2)
            elif s[i] == p[j] or p[j] == ".":
                return backtrack(i+1, j+1)
    
            return False
        
        return backtrack(0, 0)


from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        
        @cache
        def backtrack(i, j):
            if j == m: # is pattern is at the end, return true only is s is also at the end
                return i == n
            
            char_match = i < n and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < m and p[j + 1] == "*":
                zero_match_case = backtrack(i, j + 2) # 0 match case
                one_or_more_match_case = char_match and backtrack(i + 1, j)
                return zero_match_case or one_or_more_match_case
            
            elif char_match:
                return backtrack(i + 1, j + 1)
    
            return False
        
        return backtrack(0, 0)