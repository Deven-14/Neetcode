class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        operators = "+-*/"
        for token in tokens:
            if token in operators: # * token.isnumeric() and token.isdigit() won't work because of negative numbers
                b, a = stack.pop(), stack.pop()
                result = operations[token](a, b)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()