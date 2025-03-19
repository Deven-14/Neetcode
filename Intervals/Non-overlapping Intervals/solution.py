class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        i, n = 1, len(intervals)
        prev_interval = intervals[0]
        count = 0

        while i < n:
            interval = intervals[i]

            if prev_interval[1] > interval[0]:
                count += 1
                if prev_interval[1] > interval[1]:
                    prev_interval = interval
            else:
                prev_interval = interval
        
            i += 1
        
        return count


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        i, n = 1, len(intervals)
        prev_end = intervals[0][1]
        count = 0

        while i < n:
            (start, end) = intervals[i]

            if prev_end > start:
                count += 1
                if prev_end > end:
                    prev_end = end
            else:
                prev_end = end
        
            i += 1
        
        return count


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1]) # sort by end

        i, n = 1, len(intervals)
        prev_end = intervals[0][1]
        count = 0

        print(intervals)
        for i in range(1, n):
            (start, end) = intervals[i]

            if prev_end > start:
                count += 1 # prev_end will always be lesser than end coz list is sorted by end
            else:
                prev_end = end
        
        return count
            