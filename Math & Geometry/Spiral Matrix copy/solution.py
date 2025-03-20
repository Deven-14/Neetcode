class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        mul10 = 1

        num2_digits = num2[::-1]
        num1_digits = num1[::-1]
        for num2_digit in num2_digits:
            carry = 0
            num3 = 0
            mul102 = 1

            for num1_digit in num1_digits:
                total = int(num2_digit) * int(num1_digit) + carry
                carry, rem = divmod(total, 10)
                rem *= mul102
                num3 += rem
                mul102 *= 10
                print(num3, total, rem)
            
            if carry:
                carry *= mul102
                num3 += carry
            
            res += mul10 * num3 
            mul10 *= 10
        
        return str(res)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        res_10_mul = 1

        num2_digits = num2[::-1]
        num1_digits = num1[::-1]
        for num2_digit in num2_digits:
            carry = 0
            num3 = 0
            num3_10_mul = 1

            for num1_digit in num1_digits:
                total = int(num2_digit) * int(num1_digit) + carry
                carry, rem = divmod(total, 10)
                rem *= num3_10_mul
                num3 += rem
                num3_10_mul *= 10
            
            if carry:
                carry *= num3_10_mul
                num3 += carry
            
            res += res_10_mul * num3 
            res_10_mul *= 10
        
        return str(res)


