class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        combination = []
        n = len(digits)

        letters = [0, 0, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def backtrack(i):
            if i == n:
                combinations.append("".join(combination))
                return

            for letter in letters[int(digits[i])]:
                combination.append(letter)
                backtrack(i+1)
                combination.pop()
        
        if digits == "":
            return []
        backtrack(0)
        return combinations


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        combinations = [""]
        n = len(digits)

        letters = [0, 0, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        for digit in map(int, digits):
            combinations = [
                combination + letter
                for combination in combinations
                for letter in letters[digit]
            ]
        
        return combinations

