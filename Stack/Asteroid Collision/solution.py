class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if not stack or (asteroid > 0 and stack[-1] > 0) or (asteroid < 0 and stack[-1] < 0) or (asteroid > stack[-1]):
                stack.append(asteroid)
                continue
            
            abs_asteroid = abs(asteroid)
            while stack and stack[-1] > 0 and abs_asteroid > stack[-1]:
                stack.pop()
            
            if not stack:
                stack.append(asteroid)

            elif abs_asteroid == stack[-1]:
                stack.pop()
            
            elif abs_asteroid < stack[-1]:
                continue
            
            else:
                stack.append(asteroid)
        
        return stack
                
            
