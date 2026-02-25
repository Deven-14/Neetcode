from itertools import zip_longest
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = "0"
        res = ""
        for i, j in zip_longest(a[::-1], b[::-1], fillvalue="0"):
            match (i, j, carry):
                case ("0", "0", "0"):
                    res = "0" + res
                case ("0", "0", "1"):
                    res = "1" + res
                    carry = "0"
                case ("0", "1", "0") | ("1", "0", "0"):
                    res = "1" + res
                case ("0", "1", "1") | ("1", "0", "1"):
                    res = "0" + res
                    carry = "1"
                case ("1", "1", "0"):
                    res = "0" + res
                    carry = "1"
                case ("1", "1", "1"):
                    res = "1" + res
                    carry = "1"
        
        if carry == "1":
            res = "1" + res
        
        return res