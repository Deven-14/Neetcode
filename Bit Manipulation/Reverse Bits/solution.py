class Solution:
    def reverseBits(self, n: int) -> int:
        bin_num = bin(n)[2:].zfill(32)
        bin_rev_num = "".join(reversed(bin_num))
        return int(bin_rev_num, 2)


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += bit << (31 - i)
        
        return res

