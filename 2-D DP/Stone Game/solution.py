from functools import cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def dp(i, j):
            if i == j:
                return 0
            
            return max(
                piles[i] - dp(i + 1, j),
                piles[j] - dp(i, j - 1)
            )
        
        return dp(0, len(piles) - 1) > 0