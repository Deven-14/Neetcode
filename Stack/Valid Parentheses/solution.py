class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def is_open_bracket(char: str):
            return char in "({["
        
        def are_pair(open_bracket, closed_bracket):
            match (open_bracket, closed_bracket):
                case ('(', ')'):
                    return True
                case ('{', '}'):
                    return True
                case ('[', ']'):
                    return True
                case _:
                    return False
        
        for char in s:
            if is_open_bracket(char):
                stack.append(char)
            elif stack and are_pair(stack[-1], char):
                stack.pop()
            else:
                return False
        
        if stack:
            return False
        
        return True
        

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def is_open_bracket(char: str):
            return char in "({["
        
        pairs = { '(': ')', '{': '}', '[': ']' }
        
        for char in s:
            if is_open_bracket(char):
                stack.append(char)
            elif stack and pairs[stack[-1]] == char:
                stack.pop()
            else:
                return False
        
        if stack:
            return False
        
        return True
