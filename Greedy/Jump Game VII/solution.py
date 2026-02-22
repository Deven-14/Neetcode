class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        last_idx = n - 1
        i = 0

        while i < last_idx:
            best_jump = i
            for j in range(i + minJump, min(i + maxJump, last_idx) + 1):
                if s[j] == '1':
                    continue
                
                if j + minJump <= last_idx or j + maxJump <= last_idx:
                    best_jump = j
                if j == last_idx:
                    return True

            if best_jump == i:
                return False

            i = best_jump
        
        return True
            