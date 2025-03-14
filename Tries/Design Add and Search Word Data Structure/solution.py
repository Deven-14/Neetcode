class Node:
    def __init__(self, is_word_end=False):
        self.children = {}
        self.is_word_end = is_word_end


class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        node = self.head

        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        
        node.is_word_end = True

    def search(self, word: str) -> bool:

        def search_char(node, i):
            if i == len(word):
                return node.is_word_end
            
            if word[i] != ".":
                if word[i] not in node.children:
                    return False
                return search_char(node.children[word[i]], i + 1)
                
            for child_node in node.children.values():
                if search_char(child_node, i + 1):
                    return True
            
            return False

        return search_char(self.head, 0)