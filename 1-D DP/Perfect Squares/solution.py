from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        INF = float('inf')
        m = n + 1
        dp = [INF] * (m)
        dp[0] = 0
        dp[1] = 1

        squares = [i * i for i in range(1, int(sqrt(n)) + 1)]
        for square in squares:
            dp[square] = 1

        if dp[n] == 1:
            return 1
        
        for i in range(2, m):
            if dp[i] == 1:
                continue
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[square] + dp[i - square])
        
        return dp[n]
                
