class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []

        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[1] < newInterval[0]:
                new_intervals.append(interval)

            # newInterval [1, 3], [2, 5], [4, 6] -> new Inteval = [2, 5], on the left side is less than interval, on the right side is more than interval
            elif interval[0] <= newInterval[0] <= interval[1] or interval[0] <= newInterval[1] <= interval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

            elif interval[0] > newInterval[1]:
                new_intervals.append(newInterval)
                new_intervals.extend(intervals[i:])
                break
        
        else:
            new_intervals.append(newInterval) # if break not encountered
        
        return new_intervals


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        i, n = 0, len(intervals)

        while i < n and newInterval[0] > intervals[i][1]:
            new_intervals.append(intervals[i])
            i += 1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        new_intervals.append(newInterval)
        new_intervals.extend(intervals[i:])
        
        return new_intervals
