class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        prev = 0
        integer = 0
        for char in s:
            curr = roman_to_int[char]
            integer += curr
            if prev < curr:
                integer -= 2 * prev
            prev = curr
        
        return integer
