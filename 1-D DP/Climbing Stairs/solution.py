class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        step1_ways, step2_ways = 1, 2
        for _ in range(3, n+1):
            step1_ways, step2_ways = step2_ways, step1_ways + step2_ways
        
        return step2_ways