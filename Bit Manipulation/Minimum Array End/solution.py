class Solution:
    def minEnd(self, n: int, x: int) -> int:
        if n == 1:
            return x
        
        n = n-1 # coz 1st number is x
        # we need to fill 0's with the n'th number needed
        res = x
        i = 0
        while n:
            if res & (1 << i) == 0:
                bitn = (n & 1)
                res |= (bitn << i)
                n >>= 1
            i += 1
        
        return res

        