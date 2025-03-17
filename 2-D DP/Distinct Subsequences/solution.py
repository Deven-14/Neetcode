from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        
        @cache
        def backtrack(i, j):
            if j == m:
                return 1
            
            if i == n:
                return 0
            
            if s[i] == t[j]:
                return backtrack(i+1, j+1) + backtrack(i+1, j)
            
            return backtrack(i+1, j)
        
        return backtrack(0, 0)


# * Converting the above recursive solution to a bottom-up DP solution

from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n+1):
            dp[i][m] = 1 # replicated j == m: return 1 condition
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        
        return dp[0][0]


# * Good example of converting a recursive solution to a bottom-up DP solution
# * The recursive solution is easier to understand and write
