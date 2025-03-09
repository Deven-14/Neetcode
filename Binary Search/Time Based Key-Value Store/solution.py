from collections import defaultdict
from operator import itemgetter
import bisect
class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timestamps[key]
        idx = bisect.bisect_right(values, timestamp, key=itemgetter(0)) # b_right because "le" less than or equal to acc. to documentation
        if idx: # when idx == 0, skipped
            return values[idx-1][1]
        
        return ""
