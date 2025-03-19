from functools import cache
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        if x == 1:
            return 1
        
        if n == 1:
            return x
        
        @cache
        def helper(n):
            if n == 0:
                return 1
            
            if n == 2:
                return x * x
            
            if n % 2 == 0:
                value = helper(n // 2) # x^even => value = x^(even//2) => value * value = x^even
                return value * value
            
            else:
                return x * helper(n - 1) # if x^odd, = x * helper(x^even)
        
        if n < 0:
            return 1 / helper(abs(n))
        
        return helper(n)
            
        
from functools import cache
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        res = 1
        power = abs(n)

        while power:
            if power & 1: # if odd
                res *= x
            
            x *= x
            power >>= 1 # power = power >> 1 # division by 2
        
        return res if n >= 0 else 1 / res
        
