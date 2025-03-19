"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.end) # sort by end, to remove the lowest overlapping intervals # see question "Non-overlapping Intervals"
        queue = deque(intervals)
        days = 0

        while queue:
            curr_day_queue = queue
            next_day_queue = deque()
            days += 1

            prev_interval = curr_day_queue.popleft()
            while curr_day_queue:
                interval = curr_day_queue.popleft()
                
                if prev_interval.end > interval.start:
                    next_day_queue.append(interval)
                else:
                    prev_interval = interval
            
            queue = next_day_queue
        
        return days


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]

        # we have to find at any moment what is the max number of meetings going on at the same time
        # that max number will be the same as number of days would be required to complete all the meetings
        # as if 3 meetings clash, they will require 3 separate days to run the meetings at the same time

        start.sort()
        end.sort()

        s = e = 0
        n = len(intervals)
        min_days_required = days = 0

        while s < n:
            if start[s] < end[e]:
                s += 1
                days += 1
            else:
                e += 1
                days -= 1
            
            min_days_required = max(days, min_days_required) # max, as that would be the mininum required
        
        return min_days_required


