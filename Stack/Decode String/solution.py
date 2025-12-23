class Solution:

    def get_bracket_pairs(self, s):
        stack = []
        bracket_pairs = {}

        for i, char in enumerate(s):
            if char == '[':
                stack.append(i)
            elif char == ']':
                bracket_pairs[stack.pop()] = i # s is well formed

        return bracket_pairs            


    def expand_encoded_string(self, s, bracket_pairs, start, stop):
        decoded_string = []

        i = start
        while i < stop:
            
            while i < stop and s[i].isalpha():
                decoded_string.append(s[i])
                i += 1
            
            num = 0
            while i < stop and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            
            if i < stop and s[i] == '[':
                open_bracket_idx, close_bracket_idx = i, bracket_pairs[i]
                sub_str = self.expand_encoded_string(s, bracket_pairs, open_bracket_idx + 1, close_bracket_idx)
                decoded_string.append(num * sub_str)
                i = close_bracket_idx + 1
            
            else:
                i += 1
        
        return "".join(decoded_string)


    def decodeString(self, s: str) -> str:
        bracket_pairs = self.get_bracket_pairs(s)
        return self.expand_encoded_string(s, bracket_pairs, 0, len(s))
    



class Solution:

    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        num = 0
        string = ""

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                string_stack.append(string)
                count_stack.append(num)
                num = 0
                string = ""
            elif char == ']':
                count = count_stack.pop()
                string = string_stack.pop() + count * string
            else:
                string += char
        
        return string
