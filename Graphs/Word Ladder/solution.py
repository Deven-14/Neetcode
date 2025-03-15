from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        
        n = len(beginWord)
        words = set(wordList)
        queue = deque([beginWord])
        transformations = 1


        def queue_matching_words(queue, word, words):
            for i in range(n):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + char + word[i+1:]
                    if new_word in words:
                        queue.append(new_word)
                        words.remove(new_word)


        while queue and endWord in words:
            curr_level_queue = queue
            queue = deque()
            transformations += 1

            while curr_level_queue:
                word = curr_level_queue.popleft()
                queue_matching_words(queue, word, words)
        
        if endWord in words:
            return 0

        return transformations


from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        
        n = len(beginWord)
        words = set(wordList)

        patterns = defaultdict(list)
        pattern_words = defaultdict(list)

        # generate patterns
        for word in wordList + [beginWord]:
            for i in range(n):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[word].append(pattern)
                pattern_words[pattern].append(word)
                
        def queue_matching_words(queue, word, words):
            for pattern in patterns[word]:
                for matching_word in pattern_words[pattern]:
                    if matching_word in words:
                        queue.append(matching_word)
                        words.remove(matching_word)


        queue = deque([beginWord])
        transformations = 1
        while queue and endWord in words:
            curr_level_queue = queue
            queue = deque()
            transformations += 1

            while curr_level_queue:
                word = curr_level_queue.popleft()
                queue_matching_words(queue, word, words)
        
        if endWord in words:
            return 0

        return transformations


