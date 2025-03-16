from collections import defaultdict
from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        char_dict = defaultdict(list)

        for word in wordDict:
            char_dict[word[0]].append(word)
        
        @cache
        def dfs(s):
            if not s:
                return True
            
            for word in char_dict[s[0]]:
                if s.startswith(word) and dfs(s.removeprefix(word)):
                    return True

            return False
        
        return dfs(s)