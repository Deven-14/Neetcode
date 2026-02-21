
# ! confused with another question and did the above solution, though it works, this is for Stone III

from functools import cache
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)

        @cache
        def dp(i, ac, bc, alice_turn):
            if i == n:
                return abs(ac - bc)
            
            if alice_turn:
                return min(
                    dp(i + 1, ac + stones[i], bc, not alice_turn),
                    float('inf') if i+1 >= n else dp(i + 2, ac + stones[i] + stones[i + 1], bc, not alice_turn),
                    float('inf') if i+2 >= n else dp(i + 3, ac + stones[i] + stones[i + 1] + stones[i + 2], bc, not alice_turn)
                )

            return min(
                dp(i + 1, ac, bc + stones[i], not alice_turn),
                float('inf') if i+1 >= n else dp(i + 2, ac, bc + stones[i] + stones[i + 1], not alice_turn),
                float('inf') if i+2 >= n else dp(i + 3, ac, bc + stones[i] + stones[i + 1] + stones[i + 2], not alice_turn)
            )
        
        return dp(0, 0, 0, True)



# * correct solution

from functools import cache
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)

        @cache
        def dp(i, ac, bc):
            if i == n:
                return abs(ac - bc)
            
            return min(
                dp(i + 1, ac + stones[i], bc),
                dp(i + 1, ac, bc + stones[i])
            )

        return dp(0, 0, 0)



from functools import cache
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        target = total // 2

        @cache
        def dp(i, weight):
            if i == n or weight >= target:
                return abs(weight - (total - weight))
            
            return min(
                dp(i + 1, weight + stones[i]),
                dp(i + 1, weight)
            )

        return dp(0, 0)
        

