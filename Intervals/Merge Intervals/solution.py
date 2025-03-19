class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_intervals = []

        new_interval = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]

            if new_interval[1] < interval[0]:
                new_intervals.append(new_interval)
                new_interval = interval

            else:
                new_interval[0] = min(interval[0], new_interval[0])
                new_interval[1] = max(interval[1], new_interval[1])

        new_intervals.append(new_interval)
        return new_intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_intervals = []

        new_interval = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]

            if new_interval[1] < interval[0]:
                new_intervals.append(new_interval)
                new_interval = interval

            else: # as the array is sorted, we don't need to check [0] 
                new_interval[1] = max(interval[1], new_interval[1])

        new_intervals.append(new_interval)
        return new_intervals