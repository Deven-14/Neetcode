from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        cycles = 0
        queue = deque()

        while max_heap or queue:
            cycles += 1

            if max_heap:
                task_count = - heapq.heappop(max_heap)
                task_count -= 1
                task_cooldown = cycles + n
                if task_count > 0:
                    queue.append([task_count, task_cooldown])
            
            else: # if nothing in heap, then we pick the next far task from the queue
                task_count, task_cooldown = queue.popleft()
                heapq.heappush(max_heap, -task_count)
                cycles = task_cooldown 
                # task_cycle > cycles, coz if it were less it would have poped out in the below condition earlier

            # if there is a queued task which should run at AFTER this cycle (i.e., after cooldown) add it to the heap
            if queue and queue[0][1] == cycles: 
                task_count, task_cooldown = queue.popleft()
                heapq.heappush(max_heap, -task_count) # this task has to be asfter the task_cycle count

        return cycles
            
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = [0] * 26
        ord_A = ord('A')
        for task in tasks:
            task_counts[ord(task) - ord_A] += 1
        
        max_count = max(task_counts)
        no_of_task_with_max_count = 0
        for task_count in task_counts:
            no_of_task_with_max_count += 1 if task_count == max_count else 0
        
        cycles = (max_count - 1) * (n + 1) + no_of_task_with_max_count
        # (max_count - 1) coz we can do the first task immediately, we have to wait for the next identical task
        # (n + 1) coz n + 1 is the time at which the next task runs, if the earlier task ran at 1st position
        # no_of_task_with_max_count will account for the inital run eg: (1, 2) in (1, 2),... (5, 6)... (7, 8)

        return max(len(tasks), cycles) # if n is small then it could be completed with the len(tasks)