from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([(target, 0)])
        deadends = set(deadends)

        def step_up(str_num):
            return str((int(str_num) + 1) % 10)
        
        def step_down(str_num):
            return str((int(str_num) - 1 + 10) % 10)

        visited = set()
        while queue:
            step, count = queue.popleft()

            if step in deadends or step in visited:
                continue
            
            if step == "0000":
                return count
            
            visited.add(step)
            queue.append((step[:3] + step_up(step[3]), count + 1))
            queue.append((step[:3] + step_down(step[3]), count + 1))

            queue.append((step[:2] + step_up(step[2]) + step[3], count + 1))
            queue.append((step[:2] + step_down(step[2]) + step[3], count + 1))
            
            queue.append((step[0] + step_up(step[1]) + step[2:], count + 1))
            queue.append((step[0] + step_down(step[1]) + step[2:], count + 1))

            queue.append((step_up(step[0]) + step[1:], count + 1))
            queue.append((step_down(step[0]) + step[1:], count + 1))

        return -1

# if it's hard to go from outside to inside (0000 -> target)
# go from inside to outside (target -> 0000)
            