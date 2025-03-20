import math
class Solution:
    def reverse(self, x: int) -> int:
        MAX = (1 << 31) - 1
        MIN = -(1 << 31)

        MAX_div_10 = MAX // 10
        MAX_mod_10 = MAX % 10
        MIN_div_10 = MIN // 10
        MIN_mod_10 = MIN % 10


        res = 0
        while x:
            digit = int(math.fmod(x, 10)) # python issues, -1 % 10 = 9, fmod(-1, 10) = -1
            x = int(x / 10) # python issues, -1 // 10 = -1, int(x / 10) = 0

            if (res > MAX_div_10 or (res == MAX_div_10 and digit > MAX_mod_10)):
                return 0
            
            if (res < MIN_div_10 or (res == MIN_div_10 and digit < MIN_mod_10)):
                return 0
            
            res = (res * 10) + digit
        
        return res


class Solution:
    def reverse(self, x: int) -> int:
        MAX = (1 << 31) - 1

        MAX_div_10 = MAX // 10
        last_digit_for_pos = MAX % 10
        last_digit_for_neg = 8 # as -2147483648

        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1

        res = 0
        while x:
            digit = x % 10
            x //= 10

            if not is_negative and (res > MAX_div_10 or (res == MAX_div_10 and digit > last_digit_for_pos)):
                return 0
            
            elif is_negative and (res > MAX_div_10 or (res == MAX_div_10 and digit > last_digit_for_neg)):
                return 0
            
            res = (res * 10) + digit
        
        return res if not is_negative else -res

