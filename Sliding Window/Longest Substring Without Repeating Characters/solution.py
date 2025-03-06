from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_char_queue = deque()
        duplicates = set()
        max_length = 0

        for char in s:
            if char not in duplicates:
                unique_char_queue.append(char)
                duplicates.add(char)
                max_length = max(max_length, len(unique_char_queue))

            else:
                while (dup_char := unique_char_queue.popleft()) != char:
                    duplicates.remove(dup_char)
                unique_char_queue.append(char)

        return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = set()
        max_length = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            if char not in duplicates:
                duplicates.add(char)
                max_length = max(max_length, right - left + 1)

            else:
                while char in duplicates:
                    duplicates.remove(s[left])
                    left += 1
                duplicates.add(char)

        return max_length
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            if char in char_map:
                left = max(left, char_map[char] + 1)
            char_map[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length