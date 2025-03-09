import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        max_k = max(piles) # h == n

        # it should be between [1, maxk], so use binary split, mid, to identify the time

        l, r = 1, max_k
        while l < r:
            k_mid = l + (r - l) // 2
            time_to_eat = sum(
                math.ceil(nbananas / k_mid)
                for nbananas in piles
            )
            
            # using lower bound technique of binary search

            if time_to_eat > h: # we will have to increase k in this scenario, so l = mid + 1
                l = k_mid + 1
            else: # time_to_eat <= target
                r = k_mid
        
        return r # it is r instead of left coz we interchanged the conditions, considering lower bound technique of binary search
            

