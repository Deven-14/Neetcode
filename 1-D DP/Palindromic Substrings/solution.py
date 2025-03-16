class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        palindromic_substrings = n

        # for single chars
        for i in range(n):
            dp[i][i] = True
        
        # for 2 chars
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                palindromic_substrings += 1
        
        # for more than 2 chars
        for l in range(3, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1 # last index of the sub string
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    palindromic_substrings += 1
        
        return palindromic_substrings
    

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        palindromic_substrings = 0

        def get_palindrome(i, j):
            c = 0
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                c += 1
            return c
        
        for i in range(n-1):
            palindromic_substrings += get_palindrome(i, i)
            palindromic_substrings += get_palindrome(i, i+1)
        
        if n > 0:
            palindromic_substrings += 1 # coz of the (n-1)
        
        return palindromic_substrings
    
# time complexity: O(n^2)
# space complexity O(n^2)


# Manacher's Algorithm

class Solution:
    def countSubstrings(self, s: str) -> int:
        # manacher's algorithm
        T = '#' + '#'.join(list(s)) + '#' # transformed s to help with even length palindrome
        n = len(T)
        P = [0] * n # longest palindrome array
        C, R = 0, 0 # center and right edge of the current longest palindrome

        for i in range(n):
            mirror = 2 * C - i

            if i < R: # if current is less than right edge
                P[i] = min(R - i, P[mirror])
            
            while i - P[i] - 1 >= 0 and i + P[i] + 1 < n and T[i - P[i] - 1] == T[i + P[i] + 1]:
                P[i] += 1
            
            if i + P[i] > R:
                C, R = i, i + P[i]
        
        count = 0
        for length in P:
            count += (length + 1) // 2
        
        return count
    
# time complexity: O(n)
# space complexity: O(n)
