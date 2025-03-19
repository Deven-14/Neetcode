from functools import cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        @cache
        def dfs(i, open_brackets):
            if open_brackets < 0:
                return False
            
            if i == n:
                return open_brackets == 0
            
            if s[i] == "(":
                return dfs(i+1, open_brackets + 1)
            elif s[i] == ")":
                return dfs(i+1, open_brackets - 1)
            
            return (dfs(i+1, open_brackets) or dfs(i+1, open_brackets + 1) or dfs(i+1, open_brackets - 1))
        
        return dfs(0, 0)

# Time complexity: O(n^2), coz i -> [0, n-1] and open_brackets -> [0, n], so O(n^2)
# Space complexity: O(n^2)

class Solution:
    def checkValidString(self, s: str) -> bool:
        parenthesis_stack = []
        star_stack = []

        for i, char in enumerate(s):
            if char == "(":
                parenthesis_stack.append(i)
            elif char == "*":
                star_stack.append(i)
            elif parenthesis_stack: # on ")"
                parenthesis_stack.pop()
            elif star_stack: # on ")" if no open parenthesis
                star_stack.pop()
            else:
                return False
        
        while parenthesis_stack and star_stack and parenthesis_stack[-1] < star_stack[-1]:
            parenthesis_stack.pop()
            star_stack.pop()
        
        if parenthesis_stack:
            return False
        
        return True
        

# Time complexity: O(n)
# Space complexity: O(n)

