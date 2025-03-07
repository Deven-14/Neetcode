from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        left = 0
        window_char_counts = Counter(s2[:len(s1)])
        
        if s1_counts == window_char_counts:
            return True
        
        for right in range(len(s1), len(s2)):
            window_char_counts[s2[left]] -= 1
            left += 1
            window_char_counts[s2[right]] += 1

            if s1_counts == window_char_counts:
                return True
            
        return False
    

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_counts = [0] * 26
        left = 0
        window_char_counts = [0] * 26
        
        ord_a = ord('a')
        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord_a] += 1
            window_char_counts[ord(s2[i]) - ord_a] += 1

        char_matches = 0
        for i in range(26):
            char_matches += (1 if s1_counts[i] == window_char_counts[i] else 0)

        if char_matches == 26:
            return True
        
        for right in range(len(s1), len(s2)):
            index = ord(s2[left]) - ord_a
            window_char_counts[index] -= 1
            if window_char_counts[index] == s1_counts[index]:
                char_matches += 1
            elif window_char_counts[index] + 1 == s1_counts[index]:
                char_matches -= 1
            
            index = ord(s2[right]) - ord_a
            window_char_counts[index] += 1
            if window_char_counts[index] == s1_counts[index]:
                char_matches += 1
            elif window_char_counts[index] - 1 == s1_counts[index]:
                char_matches -= 1
            
            left += 1

            if char_matches == 26:
                return True
            
        return False