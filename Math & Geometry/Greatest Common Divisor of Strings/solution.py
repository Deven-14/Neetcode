from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        l1, l2 = len(str1), len(str2)
        divisor = gcd(l1, l2)
        return str1[:divisor]
