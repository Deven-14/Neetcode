class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = { char: idx for idx, char in enumerate(order) }
        
        def dfs(i, j):
            if i == len(words):
                return True
            
            n, m = len(words[i]), len(words[i-1])
            if j == n == m:
                return True
            
            elif j == m and j < n:
                return True
            
            elif j == n and j < m:
                return False

            elif order_map[words[i-1][j]] > order_map[words[i][j]]:
                return False
            
            elif order_map[words[i-1][j]] == order_map[words[i][j]]:
                return dfs(i, j+1)
            
            return dfs(i + 1, 0)

        if len(words) == 1:
            return True
        
        return dfs(1, 0)



class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = { char: idx for idx, char in enumerate(order) }
        
        def dfs(i, j):
            if i == len(words):
                return True
            
            n, m = len(words[i]), len(words[i-1])
            if m == j <= n:
                return True
            
            elif j == n and j < m:
                return False

            om, on = order_map[words[i-1][j]], order_map[words[i][j]]
            if om > on:
                return False
            
            elif om == on:
                return dfs(i, j+1) and dfs(i+1, 0)
            
            return dfs(i + 1, 0)

        if len(words) == 1:
            return True
        
        return dfs(1, 0)


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = { char: idx for idx, char in enumerate(order) }
        
        def dfs(i, j):
            if i == len(words):
                return True
            
            n, m = len(words[i]), len(words[i-1])
            if m == j <= n:
                return True
            
            elif j == n and j < m:
                return False

            om, on = order_map[words[i-1][j]], order_map[words[i][j]]
            if om > on:
                return False
            
            elif om == on:
                return dfs(i, j+1)
            
            return dfs(i + 1, 0) # om < on

        if len(words) == 1:
            return True
        
        return dfs(1, 0)

        