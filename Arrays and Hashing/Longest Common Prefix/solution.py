class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = min(strs)
        common_prefix = ""
        for i in range(len(word)):
            if not all(word[i] == string[i] for string in strs):
                return common_prefix
            common_prefix += word[i]
        
        return common_prefix
    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = min(strs)

        for i in range(len(word)):
            if not all(word[i] == string[i] for string in strs):
                return word[:i]
        
        return word