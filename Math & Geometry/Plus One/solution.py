class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []

        add_idx = len(digits)-1
        if digits[-1] == 9:
            i = len(digits) - 1
            while i >= 0 and digits[i] == 9:
                output.append(0)
                i -= 1
            
            if i < 0:
                output.append(1)
                return output[::-1]
            
            add_idx = i
            
        output.append(digits[add_idx] + 1)
        if add_idx - 1 >= 0:
            output.extend(digits[add_idx-1::-1])

        return output[::-1]


