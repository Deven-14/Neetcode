class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined_word = []
        for i in range(min(len(word1), len(word2))):
            combined_word.append(word1[i])
            combined_word.append(word2[i])
        
        if len(word1) > len(word2):
            combined_word.extend(word1[i+1:])
        
        if len(word2) > len(word1):
            combined_word.extend(word2[i+1:])
        
        return "".join(combined_word)