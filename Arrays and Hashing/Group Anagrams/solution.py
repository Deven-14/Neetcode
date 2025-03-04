from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        ord_a = ord('a')
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord_a] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())
        