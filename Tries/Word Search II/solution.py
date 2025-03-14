class Node:
    def __init__(self, is_word_end=False, word_idx=0):
        self.children = {}
        self.is_word_end = is_word_end
        self.word_idx = word_idx

class PrefixTree:
    def __init__(self, words):
        self.head = Node()

        self.words = words
        for i in range(len(words)):
            self._add(i)
    
    def _add(self, i):
        node = self.head
        for char in self.words[i]:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_word_end = True
        node.word_idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefix_tree = PrefixTree(words)
        n = len(board)
        m = len(board[0])
        found_words = set()

        def check_backtrack(i, j, node, visited=set()):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 
            
            if (i, j) in visited:
                return 

            char = board[i][j]
            if board[i][j] not in node.children:
                return 
            
            visited.add((i, j))

            node = node.children[char]
            if node.is_word_end:
                word = words[node.word_idx]
                found_words.add(word)
            
            paths = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for (x, y) in paths:
                check_backtrack(x, y, node, visited)
            
            visited.remove((i, j))
        
        for i in range(n):
            for j in range(m):
                check_backtrack(i, j, prefix_tree.head)
        
        return list(found_words)


class Node:
    def __init__(self):
        self.children = {}
        self.word_idx = -1
        self.refs = 0

class PrefixTree:
    def __init__(self, words):
        self.head = Node()

        self.words = words
        for i, word in enumerate(words):
            self._add(word, i)
            
    def _add(self, word, i):
        node = self.head
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
            node.refs += 1
        node.word_idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefix_tree = PrefixTree(words)

        n = len(board)
        m = len(board[0])
        found_words = []

        def check_backtrack(i, j, node, visited=set()):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 
            
            if (i, j) in visited:
                return 

            char = board[i][j]
            if board[i][j] not in node.children:
                return 
            
            visited.add((i, j))

            prev = node
            node = node.children[char]
            if node.word_idx != -1:
                word = words[node.word_idx]
                found_words.append(word)
                node.word_idx = -1
                node.refs -= 1
                if node.refs == 0:
                    del prev.children[char]
                    visited.remove((i, j))
                    return

            paths = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for (x, y) in paths:
                check_backtrack(x, y, node, visited)
            
            visited.remove((i, j))
        
        for i in range(n):
            for j in range(m):
                check_backtrack(i, j, prefix_tree.head)
        
        return found_words