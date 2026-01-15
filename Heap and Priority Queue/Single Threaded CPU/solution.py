import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        min_heap_tasks = []
        for idx, (enqueue_time, processing_time) in enumerate(tasks):
            min_heap_tasks.append((enqueue_time, processing_time, idx))
        heapq.heapify(min_heap_tasks)
        
        min_heap_arrived = []
        order = []
        current_time = min_heap_tasks[0][0]
        while min_heap_tasks or min_heap_arrived:

            while min_heap_tasks and min_heap_tasks[0][0] <= current_time:
                (enqueue_time, processing_time, idx) = heapq.heappop(min_heap_tasks)
                heapq.heappush(min_heap_arrived, (processing_time, idx))
            
            if min_heap_arrived:
                processing_time, idx = heapq.heappop(min_heap_arrived)
                current_time += processing_time
                order.append(idx)
        
            elif min_heap_tasks and min_heap_tasks[0][0] > current_time:
                current_time = min_heap_tasks[0][0]

        return order




import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [task + [i] for i, task in enumerate(tasks)]
        tasks.sort(key=lambda x: x[0]) # sort on enqueue time
        i, n = 0, len(tasks)
        
        min_heap = []
        order = []
        current_time = tasks[0][0]

        while i < n or min_heap:

            while i < n and tasks[i][0] <= current_time:
                (enqueue_time, processing_time, idx) = tasks[i]
                heapq.heappush(min_heap, (processing_time, idx))
                i += 1
            
            if min_heap:
                processing_time, idx = heapq.heappop(min_heap)
                current_time += processing_time
                order.append(idx)
        
            else:
                current_time = tasks[i][0]

        return order
    


