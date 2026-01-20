class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        n = len(matchsticks)
        side_length = total // 4
        if total / 4 != side_length or len(matchsticks) < 4 or any(ele > side_length for ele in matchsticks):
            return False
        
        visited = [False] * n
        matchsticks.sort(reverse=True)

        def backtracking(side, length):
            if side == 4:
                return True
            
            if length == side_length:
                return backtracking(side + 1, 0)
            elif length > side_length:
                return False
            
            for i, matchstick in enumerate(matchsticks):
                if visited[i]:
                    continue
                
                visited[i] = True
                if backtracking(side, length + matchstick):
                    return True
                visited[i] = False
            
            return False
        
        return backtracking(0, 0)
                    
                        
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        n = len(matchsticks)
        side_length = total // 4
        if total % 4 != 0 or len(matchsticks) < 4 or max(matchsticks) > side_length:
            return False
        
        visited = [False] * n
        matchsticks.sort(reverse=True)

        def backtracking(side, length):
            if side == 4:
                return True
            
            if length == side_length:
                return backtracking(side + 1, 0)
            elif length > side_length:
                return False
            
            for i, matchstick in enumerate(matchsticks):
                if visited[i]:
                    continue
                
                visited[i] = True
                if backtracking(side, length + matchstick):
                    return True
                visited[i] = False
            
            return False
        
        return backtracking(0, 0)
                    
                        
            

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        n = len(matchsticks)
        side_length = total // 4
        if total % 4 != 0 or len(matchsticks) < 4 or max(matchsticks) > side_length:
            return False
        
        sides = [0] * 4
        matchsticks.sort(reverse=True) # pruning

        def backtracking(i):
            if i == n:
                return True
            
            matchstick = matchsticks[i]
            for side in range(4):
                if sides[side] == side_length or sides[side] + matchstick > side_length:
                    continue
                
                sides[side] += matchstick
                if backtracking(i + 1):
                    return True
                sides[side] -= matchstick

                if sides[side] == 0:
                    break # If the current side is empty after backtracking, stop trying other sides (they are equivalent).
            
            return False
        
        return backtracking(0)
                    
                        
            