class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = [char.lower() for char in s if char.isalnum()]
        n = len(alpha_s)

        def check_palindrome(i, j):
            while i >= 0 and j < n and alpha_s[i] == alpha_s[j]:
                i -= 1
                j += 1
            
            if j == n:
                return True
            
            return False

        if n % 2 == 0:
            mid = n // 2
            return check_palindrome(mid-1, mid)

        else:
            mid = n // 2
            return check_palindrome(mid, mid)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = [char.lower() for char in s if char.isalnum()]
        n = len(alpha_s)
        mid = n // 2
        return alpha_s[:mid] == alpha_s[:-mid-1:-1]
         