class Node:
    def __init__(self, char="", word_end=False):
        self.char = char
        self.next_chars = [None] * 26
        self.word_end = word_end

class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        node = self.head
        for char in word:
            char_idx = ord(char) - ord('a')
            if not node.next_chars[char_idx]:
                node.next_chars[char_idx] = Node(char)
            node = node.next_chars[char_idx]
        node.word_end = True

    def search(self, word: str) -> bool:
        node = self.head
        for char in word:
            char_idx = ord(char) - ord('a')
            if not node.next_chars[char_idx]:
                return False
            node = node.next_chars[char_idx]

        return node.word_end
        
    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for char in prefix:
            char_idx = ord(char) - ord('a')
            if not node.next_chars[char_idx]:
                return False
            node = node.next_chars[char_idx]

        return True


class Node:
    def __init__(self, is_word_end=False):
        self.children = [None] * 26
        self.is_word_end = is_word_end

class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        node = self.head

        for char in word:
            char_idx = ord(char) - ord('a')
            if not node.children[char_idx]:
                node.children[char_idx] = Node()
            node = node.children[char_idx]
        
        node.is_word_end = True

    def search(self, word: str) -> bool:
        node = self.head

        for char in word:
            char_idx = ord(char) - ord('a')
            if not node.children[char_idx]:
                return False
            node = node.children[char_idx]

        return node.is_word_end
        
    def startsWith(self, prefix: str) -> bool:
        node = self.head

        for char in prefix:
            char_idx = ord(char) - ord('a')
            if not node.children[char_idx]:
                return False
            node = node.children[char_idx]

        return True
        