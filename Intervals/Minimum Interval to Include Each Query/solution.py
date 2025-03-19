class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = [(start, end, end - start + 1) for (start, end) in intervals]
        intervals.sort()
        n = len(intervals)
        output = []

        for query in queries:
            
            i = 0
            min_length = float("inf")
            while i < n and query >= intervals[i][0]:
                if query <= intervals[i][1]:
                    min_length = min(min_length, intervals[i][2])
                i += 1
            
            output.append(-1 if min_length == float("inf") else min_length)
        
        return output



import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = [(start, end, end - start + 1) for (start, end) in intervals]
        intervals.sort()
        
        n = len(intervals)
        min_heap = []
        output = {}
        i = 0

        for query in sorted(queries):
            
            while i < n and query >= intervals[i][0]: # query >= start
                heapq.heappush(min_heap, (intervals[i][2], intervals[i][1]))
                i += 1
            
            while min_heap and query > min_heap[0][1]: # query > end
                heapq.heappop(min_heap)
            
            output[query] = min_heap[0][0] if min_heap else -1
        
        return [output[query] for query in queries]


