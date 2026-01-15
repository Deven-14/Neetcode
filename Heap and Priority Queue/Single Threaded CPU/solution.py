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