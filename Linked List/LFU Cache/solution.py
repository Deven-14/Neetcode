from collections import Counter, OrderedDict, defaultdict
import heapq

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counts = Counter()
        self.cache = defaultdict(OrderedDict)
        self.min_heap = []

    def get(self, key: int) -> int:
        if key not in self.counts:
            return -1
        
        count = self.counts[key]
        value = self.cache[count][key]
        del self.cache[count][key]
        if not self.cache[count]:
            del self.cache[count]

        count += 1
        self.counts[key] = count
        if count not in self.cache:
            heapq.heappush(self.min_heap, count)
        
        self.cache[count][key] = value
        self.cache[count].move_to_end(key)

        return value

    def put(self, key: int, value: int) -> None:
        if len(self.counts) == self.capacity:
            while self.min_heap[0] not in self.cache:
                heapq.heappop(self.min_heap)
        
            count = self.min_heap[0]
            del_key, _ = self.cache[count].popitem(last=False)
            del self.counts[del_key]
            if not self.cache[count]:
                del self.cache[count]

        if key in self.counts:
            count = self.counts[key]
            del self.cache[count][key]
            if not self.cache[count]:
                del self.cache[count]

        self.counts[key] += 1
        count = self.counts[key]
        if count not in self.cache:
            heapq.heappush(self.min_heap, count)

        self.cache[count][key] = value
        self.cache[count].move_to_end(key)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



from collections import Counter, OrderedDict, defaultdict
import heapq

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counts = Counter()
        self.cache = defaultdict(OrderedDict)
        self.min_count = 0

    def counter(self, key):
        count = self.counts[key]
        value = self.cache[count][key]
        del self.cache[count][key]

        if count == self.min_count and len(self.cache[count]) == 0:
            self.min_count += 1

        count += 1
        self.counts[key] = count    
        self.cache[count][key] = value
        self.cache[count].move_to_end(key)
        return count

    def get(self, key: int) -> int:
        if key not in self.counts:
            return -1
        
        count = self.counter(key)
        return self.cache[count][key]

    def put(self, key: int, value: int) -> None:
        if len(self.counts) == self.capacity and key not in self.counts:
            del_key, _ = self.cache[self.min_count].popitem(last=False)
            del self.counts[del_key]

        if key not in self.counts:
            count = 1
            self.counts[key] = count
            self.min_count = count
            self.cache[count][key] = value
            self.cache[count].move_to_end(key)
            return

        count = self.counter(key)
        self.cache[count][key] = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)