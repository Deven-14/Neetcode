from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1 # 1 way to arrange nothing
        dp[1] = 1 # 1 way to arrange 1 number

        for i in range(2, n+1):
            one_digit = int(s[i-1]) # current digit in s, i-1 coz i ranges from [2, n+1)
            two_digits = int(s[i-2:i]) # last 2 digits

            if 1 <= one_digit <= 9:
                dp[i] = dp[i-1] # adding ways from single digit decoding
                # if it is not 0 then same value as previous of else 0
                # we can do += or = as dp[i] is 0 initially
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2] # adding ways from two digit decoding
                # if it is not between 01 - 09 then we can add in the no. of ways it took to decode without these 2 chars

        return dp[n]
