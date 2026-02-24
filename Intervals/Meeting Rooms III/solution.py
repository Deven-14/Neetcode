import heapq
from collections import Counter
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        i, m = 0, len(meetings)
        meetings.sort()
        meeting_rooms = list(range(n))
        min_heap = []
        meetings_count = Counter()
        min_start_time = 0

        while i < m:

            start, end = meetings[i]
            if start < min_start_time:
                # print(start, end, min_start_time)
                end += min_start_time - start

            meeting_room = heapq.heappop(meeting_rooms)
            heapq.heappush(min_heap, (end, meeting_room))
            meetings_count[meeting_room] += 1
            i += 1
            
            # print(min_heap, meeting_rooms, meetings_count)
            if i == m:
                break

            min_start_time = max(meetings[i][0], min_start_time)
            if not meeting_rooms and min_start_time < min_heap[0][0]:
                min_start_time = min_heap[0][0]

            while min_heap and min_heap[0][0] <= min_start_time:
                _, meeting_room = heapq.heappop(min_heap)
                heapq.heappush(meeting_rooms, meeting_room)
            
            # print(min_heap, meeting_rooms, meetings_count)

        return meetings_count.most_common(1)[0][0]
        
