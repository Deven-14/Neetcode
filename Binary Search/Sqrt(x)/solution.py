class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        l, r = 0, x // 2
        res = l

        while l <= r:
            mid = (l + r) // 2
            mid_square = mid * mid
            if mid_square == x:
                return mid
            elif mid_square > x:
                r = mid - 1
            else:
                res = mid
                l = mid + 1
        
        return res
    


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, (x // 2) + 1
        res = l

        while l <= r:
            mid = (l + r) // 2
            mid_square = mid * mid
            if mid_square == x:
                return mid
            elif mid_square > x:
                r = mid - 1
            else:
                res = mid
                l = mid + 1
        
        return res
    
    