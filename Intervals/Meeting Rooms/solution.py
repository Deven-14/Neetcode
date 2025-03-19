"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key=lambda interval: interval.start)
        
        prev_end = intervals[0].end
        for i in range(1, len(intervals)):
            interval = intervals[i]

            if prev_end > interval.start:
                return False
            
            prev_end = max(prev_end, interval.end)
        
        return True
            