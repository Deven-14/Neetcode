class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        def helper(n):
            if n == 1:
                return True
            
            if n in visited:
                return False
            
            visited.add(n)

            return helper(sum(int(char) ** 2 for char in str(n)))
        
        return helper(n)