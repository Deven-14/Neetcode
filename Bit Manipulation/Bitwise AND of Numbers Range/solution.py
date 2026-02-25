class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        bit = 1
        x = right & ~bit
        while x > left and res != 0:
            res &= x
            bit <<= 1
            x = right & ~bit
        
        return res


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        bit = 1
        x = right & ~bit
        for _ in range(32):
            if x > left:
                res &= x
                bit <<= 1
                x = right & ~bit
        
        return res


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        bit = 1
        x = right & ~bit
        for _ in range(32):
            if x <= left or res == 0:
                break
            res &= x
            bit <<= 1
            x = right & ~bit
        
        return res


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        return left << i


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return right

# * The operation (n & (n-1)) clears the lowest set bit of n. 