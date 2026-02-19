
# ! RecursionError: maximum recursion depth exceeded

from functools import cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        @cache
        def dp(i):
            if i >= n:
                return 0
            
            return max(
                stoneValue[i] - dp(i + 1),
                float('-inf') if i+1 >= n else stoneValue[i] + stoneValue[i+1] - dp(i + 2), 
                float('-inf') if i+2 >= n else stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp(i + 3)
            )

        res = dp(0)
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        
        return "Tie"


# * since it doesn't state that check if Alice should win, we can't use 'or' and 'and' method
# * we would have to use min max method



from functools import cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        stoneValue.append(0)
        stoneValue.append(0)
        stoneValue.append(0)
        dp = [0] * (n + 3)
        
        for i in range(n-1, -1, -1):
            dp[i] = max(
                stoneValue[i] - dp[i + 1],
                stoneValue[i] + stoneValue[i+1] - dp[i + 2], 
                stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i + 3]
            )

        res = dp[0]
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        
        return "Tie"



from functools import cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        stoneValue.append(0)
        stoneValue.append(0)
        stoneValue.append(0)
        a, b, c, d = 0, 0, 0, 0
        
        for i in range(n-1, -1, -1):
            a = max(
                stoneValue[i] - b,
                stoneValue[i] + stoneValue[i+1] - c, 
                stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - d
            )
            b, c, d = a, b, c

        res = a
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        
        return "Tie"


# * THIS TIME ONLY I USED "ITERATIVE TOP-DOWN" because
# * the recursive top-down even with caching was
# * getting into maximum recursion depth exceeded error
