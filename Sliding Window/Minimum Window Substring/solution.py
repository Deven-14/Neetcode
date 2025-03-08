class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_counts = [0] * 123 # A - Z and ... and a - z
        window_counts = [0] * 123

        ord_a = ord('A')
        for i in range(len(t)):
            t_counts[ord(t[i]) - ord_a] += 1
            window_counts[ord(s[i])- ord_a] += 1
        
        matches = 0
        for i in range(123):
            if window_counts[i] >= t_counts[i]:
                matches += 1
                
        if matches == 123:
            return s[:len(t)]

        for right in range(len(t), len(s)):
            idx = ord(s[right]) - ord_a
            window_counts[idx] += 1
            if window_counts[idx] - 1 < t_counts[i] and window_counts[idx] >= t_counts[i]:
                matches += 1
            
            if matches == 123:
                break
        
        for left in range(right):
            idx = ord(s[left]) - ord_a
            window_counts[idx] -= 1
            if window_counts[idx] < t_counts[i]:
                return s[left:right]
            
        return ""

# ! wrong solution because it doesn't handle the case where the window is not valid

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_counts = Counter(t)
        window_counts = Counter(s[:len(t)])
                
        if window_counts >= t_counts:
            return s[:len(t)]

        min_sub_string = s+t
        left = 0
        right = len(t)
        
        while left < right < len(s):
            while right < len(s) and not window_counts >= t_counts:
                char = s[right]
                window_counts[char] += 1
                right += 1
            
            while left < right and window_counts >= t_counts: 
                char = s[left]
                window_counts[char] -= 1
                left += 1
            
            if len(min_sub_string) > (right - left + 1):
                min_sub_string = s[left-1:right]
            
        return min_sub_string if min_sub_string != s+t else ""


from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_counts = Counter(t)
        window_counts = Counter(s[:len(t)])
                
        if window_counts >= t_counts:
            return s[:len(t)]

        chars_to_be_matched = len(t_counts)
        char_matches = 0
        for char in t_counts:
            if window_counts[char] >= t_counts[char]:
                char_matches += 1
        
        if char_matches == chars_to_be_matched:
            return s[:len(t)]

        min_sub_string = None
        left = 0
        right = len(t)
        while left < right < len(s):
            while right < len(s) and not char_matches == chars_to_be_matched:
                char = s[right]
                window_counts[char] += 1
                if char in t_counts and window_counts[char] >= t_counts[char] and window_counts[char]-1 < t_counts[char]:
                    char_matches += 1
                right += 1
            
            if not char_matches == chars_to_be_matched:
                break
            
            while left < right and char_matches == chars_to_be_matched:
                if not min_sub_string or len(min_sub_string) > (right - left):
                    min_sub_string = s[left:right] 
                
                char = s[left]
                window_counts[char] -= 1
                if char in t_counts and window_counts[char] < t_counts[char]:
                    char_matches -= 1
                left += 1
            
        return min_sub_string if min_sub_string != None else ""