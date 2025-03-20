class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        counts = [0] * (n + 1)
        counts[1] = 1

        prev, curr = 1 << 1, 1 << 2
        while curr <= n:
            counts[prev:curr] = [1 + count for count in counts[:prev]]
            prev, curr = curr, curr << 1
        
        curr = min(n, curr)
        counts[prev:curr+1] = [1 + count for count in counts[:curr-prev+1]]

        return counts