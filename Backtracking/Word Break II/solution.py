class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        sentences = []
        sentense = []
        
        def backtracking(substr):
            if len(substr) == 0:
                sentences.append(" ".join(sentense))
                return
            
            for word in wordDict:
                if not substr.startswith(word):
                    continue
                
                sentense.append(word)
                backtracking(substr.removeprefix(word))
                sentense.pop()
            
        backtracking(s)
        return sentences


from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        sentences = []
        sentense = []
        words = defaultdict(list)
        
        for word in wordDict:
            words[word[0]].append(word)
        
        def backtracking(substr):
            if len(substr) == 0:
                sentences.append(" ".join(sentense))
                return
            
            for word in words[substr[0]]:
                if not substr.startswith(word):
                    continue
                
                sentense.append(word)
                backtracking(substr.removeprefix(word))
                sentense.pop()
            
        backtracking(s)
        return sentences



from collections import defaultdict
from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = defaultdict(list)
        for word in wordDict:
            words[word[0]].append(word)
        
        @cache
        def backtracking(substr):
            if len(substr) == 0:
                return [""]
            
            sentences = []
            for word in words[substr[0]]:
                if not substr.startswith(word):
                    continue
                
                sub_sentences = backtracking(substr.removeprefix(word))
                for sub_sentence in sub_sentences:
                    sentence = word + " " + sub_sentence if sub_sentence else word
                    sentences.append(sentence)
            
            return sentences
            
        return backtracking(s)



from functools import cache

class Node:
    def __init__(self, is_word=False):
        self.children = {}
        self.is_word = is_word

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        
        node.is_word = True
    
    def add_words(self, words):
        for word in words:
            self.add_word(word)

    def search_prefixes(self, string):
        node = self.root
        prefix = ""

        for char in string:
            if char not in node.children:
                return
            
            node = node.children[char]
            prefix += char
            if node.is_word:
                yield prefix


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        trie.add_words(wordDict)
        n = len(s)
        
        @cache
        def backtracking(substr):
            if len(substr) == 0:
                return [""]
            
            sentences = []
            for prefix in trie.search_prefixes(substr):
                sub_sentences = backtracking(substr.removeprefix(prefix))
                for sub_sentence in sub_sentences:
                    sentence = prefix + " " + sub_sentence if sub_sentence else prefix
                    sentences.append(sentence)
            
            return sentences
            
        return backtracking(s)



from functools import cache

class Node:
    def __init__(self, is_word=False):
        self.children = {}
        self.is_word = is_word

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        
        node.is_word = True
    
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
            if node.is_word:
                yield idx


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        trie.add_words(wordDict)
        n = len(s)
        
        @cache
        def backtracking(i):
            if i == n:
                return [""]
            
            sentences = []
            for idx in trie.search_prefixes(s, i):
                sub_sentences = backtracking(idx + 1)
                prefix = s[i : idx + 1]
                for sub_sentence in sub_sentences:
                    sentence = prefix + " " + sub_sentence if sub_sentence else prefix
                    sentences.append(sentence)
            
            return sentences
            
        return backtracking(0)


