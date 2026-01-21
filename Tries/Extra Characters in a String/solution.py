from functools import cache

class Node:
    def __init__(self, is_word_end=False):
        self.children = {}
        self.is_word_end = is_word_end

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        
        node.is_word_end = True
    
    def add_words(self, words):
        for word in words:
            self.add_word(word)
    
    def search_prefixes(self, string, i):
        node = self.root

        for idx in range(i, len(string)):
            char = string[idx]
            if char not in node.children:
                return
            
            node = node.children[char]
            if node.is_word_end:
                yield idx


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        trie.add_words(dictionary)
        n = len(s)

        @cache
        def backtrack(i):
            if i == n:
                return 0

            min_extra_chars = n - i
            for idx in trie.search_prefixes(s, i):
                extra_chars = backtrack(idx + 1)
                min_extra_chars = min(min_extra_chars, extra_chars)
            
            extra_chars = 1 + backtrack(i + 1)
            min_extra_chars = min(min_extra_chars, extra_chars)

            return min_extra_chars
        
        return backtrack(0)


# * see question Word Break II to understand how I reached this logic directly
# * step by step improvement shown in that solution