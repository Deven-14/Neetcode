class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 32) - 1 # 32-bit mask (equivalent to 0xFFFFFFFF)
        max_int = (1 << 31) - 1 # Maximum positive 32-bit integer (0x7FFFFFFF)

        while b != 0:
            carry = (a & b) << 1 # Compute carry
            a = (a ^ b) & mask # Sum without carry, apply mask
            b = carry & mask # Update b to carry
        
        return a if a <= max_int else ~(a ^ mask)
        # If a is negative in 32-bit signed representation, convert it properly

# ~(a ^ mask) for negative numbers, in the while loop we were forcing it to be 32 bit number
# but by doing ~(a ^ mask), we change that to reflect a normal number
# a = 11111111 11111111 11111111 11111011 (-5) (which is -5 in two’s complement).
# a ^ mask = 00000000 00000000 00000000 00000100 (which is 4)
# ~4 = -5 (proper represenation of -5 and not 32 bit version of -5)

