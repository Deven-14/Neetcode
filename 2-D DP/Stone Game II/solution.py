from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        @cache
        def dp(i, m, alice_turn):
            if i >= n:
                return 0
        
            if alice_turn:
                max_stones = 0
                stones = 0
                count = 1
                for j in range(i, min(n, i + 2 * m)):
                    stones += piles[j]
                    max_stones = max(
                        max_stones, 
                        stones + dp(j + 1, max(count, m), not alice_turn)
                    )
                    count += 1

                return max_stones    
            
            count = 1
            min_stones = float('inf')
            for j in range(i, min(n, i + 2 * m)):
                min_stones = min(
                    min_stones, 
                    dp(j + 1, max(count, m), not alice_turn)
                )
                count += 1

            return min_stones

        return dp(0, 1, True)
