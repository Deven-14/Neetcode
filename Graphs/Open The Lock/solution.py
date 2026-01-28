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



from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([target])
        deadends = set(deadends)

        def step_up(str_num):
            return str((int(str_num) + 1) % 10)
        
        def step_down(str_num):
            return str((int(str_num) - 1 + 10) % 10)

        visited = set()
        count = 0

        while queue:
            next_queue = deque()

            while queue:
                step = queue.popleft()

                if step in deadends or step in visited:
                    continue
                
                if step == "0000":
                    return count
                
                visited.add(step)
                next_queue.append(step[:3] + step_up(step[3]))
                next_queue.append(step[:3] + step_down(step[3]))

                next_queue.append(step[:2] + step_up(step[2]) + step[3])
                next_queue.append(step[:2] + step_down(step[2]) + step[3])
                
                next_queue.append(step[0] + step_up(step[1]) + step[2:])
                next_queue.append(step[0] + step_down(step[1]) + step[2:])

                next_queue.append(step_up(step[0]) + step[1:])
                next_queue.append(step_down(step[0]) + step[1:])

            count += 1
            queue = next_queue

        return -1

# if it's hard to go from outside to inside (0000 -> target)
# go from inside to outside (target -> 0000)
            


from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start_queue = deque(["0000"])
        end_queue = deque([target])
        deadends = set(deadends)

        def step_up(str_num):
            return str((int(str_num) + 1) % 10)
        
        def step_down(str_num):
            return str((int(str_num) - 1 + 10) % 10)

        start_set = set()
        end_set = set()
        count = -1

        while start_queue or end_queue:
            if len(start_queue) == 0 or len(start_queue) > len(end_queue):
                start_queue, end_queue = end_queue, start_queue
                start_set, end_set = end_set, start_set

            next_queue = deque()
            while start_queue:
                step = start_queue.popleft()

                if step in deadends or step in start_set:
                    continue
                
                if step in end_set:
                    return count
                
                start_set.add(step)
                next_queue.append(step[:3] + step_up(step[3]))
                next_queue.append(step[:3] + step_down(step[3]))

                next_queue.append(step[:2] + step_up(step[2]) + step[3])
                next_queue.append(step[:2] + step_down(step[2]) + step[3])
                
                next_queue.append(step[0] + step_up(step[1]) + step[2:])
                next_queue.append(step[0] + step_down(step[1]) + step[2:])

                next_queue.append(step_up(step[0]) + step[1:])
                next_queue.append(step_down(step[0]) + step[1:])

            count += 1
            start_queue = next_queue

        return -1

# if it's hard to go from outside to inside (0000 -> target)
# go from inside to outside (target -> 0000)
# if we have both then go from both directions - Multi source BFS - (0000 -> <- target)  