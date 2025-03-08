class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        
        prev_parentheses_list = self.generateParenthesis(n-1)
        new_parentheses_set = set()
        for parentheses in prev_parentheses_list:
            for i in range(len(parentheses)):
                new_parentheses = parentheses[:i] + "()" + parentheses[i:]
                new_parentheses_set.add(new_parentheses)
        return list(new_parentheses_set)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = []
        parenthesis_length = n * 2

        def backtrack(s = "", n_open = 0, n_closed = 0):
            if parenthesis_length == len(s):
                parenthesis.append(s)
                return
            
            if n_open < n:
                backtrack(s + "(", n_open + 1, n_closed)
            
            if n_closed < n_open:
                backtrack(s + ")", n_open, n_closed + 1)
        
        backtrack()
        return parenthesis


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = []
        parenthesis_length = n * 2
        stack = []

        def backtrack(n_open = 0, n_closed = 0):
            if n_open == n_closed == n:
                parenthesis.append("".join(stack))
                return
            
            if n_open < n:
                stack.append("(")
                backtrack(n_open + 1, n_closed)
                stack.pop()
            
            if n_closed < n_open:
                stack.append(")")
                backtrack(n_open, n_closed + 1)
                stack.pop()
        
        backtrack()
        return parenthesis


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]

        for k in range(1, n+1):
            for i in range(k):
                for left in dp[i]:
                    for right in dp[k-i-1]:
                        dp[k].append(f"({left}){right}")
        
        return dp[-1]