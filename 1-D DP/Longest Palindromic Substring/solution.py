class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_length = 1
        start_idx = 0

        # for single chars
        for i in range(n):
            dp[i][i] = True
        
        # for 2 chars
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_length = 2
                start_idx = i
        
        # for more than 2 chars
        for l in range(3, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1 # last index of the sub string
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    max_length = l
                    start_idx = i
        
        return s[start_idx : start_idx + max_length]
    

# time complexity: O(n^2)
# space complexity: O(n^2)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def get_palindrome(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        
        max_substring = s[0]
        for i in range(n-1):
            s1 = get_palindrome(i, i)
            if len(s1) > len(max_substring):
                max_substring = s1
            
            s2 = get_palindrome(i, i+1)
            if len(s2) > len(max_substring):
                max_substring = s2
        
        return max_substring


# time complexity: O(n^2)
# space complexity: O(1)

# there is a Manacher's algorithm which can solve this problem in O(n) time complexity


class Solution:
    def longestPalindrome(self, s: str) -> str:
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
        
        # get the max length
        max_length, center = max((P[i], i) for i in range(n))
        transformed_start_idx = center - max_length
        start_idx = transformed_start_idx // 2 # original
        
        return s[start_idx : start_idx + max_length]
    
# * time complexity: O(n)
# * space complexity: O(n)



class Solution:
    def longestPalindrome(self, s: str) -> str:
        # manacher's algorithm
        T = "^#" + '#'.join(list(s)) + "#$" # transformed s to help with even length palindrome
        n = len(T)
        P = [0] * n # longest palindrome array
        C, R = 0, 0 # center and right edge of the current longest palindrome

        for i in range(1, n-1):
            mirror = 2 * C - i

            if i < R: # if current is less than right edge
                P[i] = min(R - i, P[mirror])
            
            while T[i - P[i] - 1] == T[i + P[i] + 1]:
                P[i] += 1
            
            if i + P[i] > R:
                C, R = i, i + P[i]
        
        # get the max length
        max_length, center = max((P[i], i) for i in range(n))
        transformed_start_idx = center - max_length
        start_idx = transformed_start_idx // 2 # original
        
        return s[start_idx : start_idx + max_length]