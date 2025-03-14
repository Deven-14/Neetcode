class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isplaindrome(sub_string):
            mid = len(sub_string) // 2
            return sub_string[:mid] == sub_string[:-mid-1:-1]
        
        def isplaindromes(sub_strings):
            return all(isplaindrome(sub_string) for sub_string in sub_strings)
        
        all_palindrome_substrings = []
        palindrome_substrings = []
        n = len(s)

        def backtrack(i):
            if i == n:
                if isplaindromes(palindrome_substrings):
                    all_palindrome_substrings.append(list(palindrome_substrings))
                return
            
            palindrome_substrings.append(s[i])
            backtrack(i+1)
            palindrome_substrings.pop()

            if len(palindrome_substrings) > 0:
                string = palindrome_substrings.pop()
                palindrome_substrings.append(string + s[i])
                backtrack(i+1)
        
        backtrack(0)
        return all_palindrome_substrings


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isplaindrome(i, j):
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            if i < j:
                return False
            return True
        
        all_palindrome_substrings = []
        palindrome_substrings = []
        n = len(s)

        def backtrack(i):
            if i == n:
                all_palindrome_substrings.append(list(palindrome_substrings))
                return
            
            for j in range(i, n):
                if isplaindrome(i, j):
                    palindrome_substrings.append(s[i:j+1])
                    backtrack(j+1)
                    palindrome_substrings.pop()
        
        backtrack(0)
        return all_palindrome_substrings
    

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def create_palidrome_dp():
            n = len(s)
            dp = [[False] * n for _ in range(n)]
            
            # single char
            for i in range(n):
                dp[i][i] = True
            
            # 2 chars
            for i in range(n-1):
                if s[i] == s[i+1]:
                    dp[i][i+1] = True
            
            for l in range(3, n+1): # length from 3 to n
                for i in range(n - l + 1):
                    j = i + l - 1 # last index of the sub string
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
            
            return dp

        dp = create_palidrome_dp()
        all_palindrome_substrings = []
        palindrome_substrings = []
        n = len(s)

        def backtrack(i):
            if i == n:
                all_palindrome_substrings.append(list(palindrome_substrings))
                return
            
            for j in range(i, n):
                if dp[i][j]:
                    palindrome_substrings.append(s[i:j+1])
                    backtrack(j+1)
                    palindrome_substrings.pop()
        
        backtrack(0)
        return all_palindrome_substrings
