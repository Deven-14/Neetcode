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


from collections import defaultdict
from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        t = max(len(word) for word in wordDict) # max_len
        
        @cache
        def dfs(i):
            if i == len(s):
                return True
            
            for j in range(i, min(n, i + t)):
                if s[i : j + 1] in word_set and dfs(j + 1):
                    return True

            return False
        
        return dfs(0)
    

from collections import defaultdict
from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        t = max(len(word) for word in wordDict) # max_len

        char_dict = defaultdict(set)
        for word in wordDict:
            char_dict[word[0]].add(word)
        
        @cache
        def dfs(i):
            if i == len(s):
                return True
            
            word_sub_set = char_dict[s[i]]
            for j in range(i, min(n, i + t)):
                if s[i : j + 1] in word_sub_set and dfs(j + 1):
                    return True

            return False
        
        return dfs(0)


# * similarly we can do using a trie data structure as well, instead of using word_set or word_sub_set, use trie.search() method
# * to check if the word is present in the trie or not

# TODO: try the trie approach as well and also bottom up dp approach