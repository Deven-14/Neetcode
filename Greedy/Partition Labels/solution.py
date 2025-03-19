class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars = {} # in order
        for i, char in enumerate(s):
            if char in chars:
                chars[char][1] = i
            else:
                chars[char] = [i, i]
        
        substrings = []
        prev = [0, 0]
        for char, interval in chars.items():
            if interval[0] <= prev[1]:
                prev = [prev[0], max(interval[1], prev[1])]
            else:
                substrings.append(prev[1] - prev[0] + 1)
                prev = interval
        
        substrings.append(prev[1] - prev[0] + 1)
        return substrings


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurances = {}
        for i, char in enumerate(s):
            last_occurances[char] = i
        
        substrings = []
        size = last_occurance = 0
        for i, char in enumerate(s):
            size += 1
            last_occurance = max(last_occurance, last_occurances[char])

            if i == last_occurance:
                substrings.append(size)
                size = 0
        
        return substrings

