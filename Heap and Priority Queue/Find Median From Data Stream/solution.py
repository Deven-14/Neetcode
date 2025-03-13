class MedianFinder:

    def __init__(self):
        self.max_heap = [] # for the left side of the tree (smaller values)
        self.min_heap = [] # for the right side of the tree (larger values)
        self.median = None

    def add_to_max_heap(self, num):
        if len(self.max_heap) > len(self.min_heap):
            larger_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, larger_num)
            
        heapq.heappush(self.max_heap, -num)
    
    def add_to_min_heap(self, num):
        if len(self.min_heap) > len(self.max_heap):
            smaller_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -smaller_num)
        
        heapq.heappush(self.min_heap, num)

    def addNum(self, num: int) -> None:
        if not self.max_heap and not self.min_heap:
            self.add_to_max_heap(num)
            return
        
        elif not self.min_heap:
            if num > -self.max_heap[0]:
                self.add_to_min_heap(num)
            else:
                self.add_to_max_heap(num)
            return
        
        left = -self.max_heap[0]
        right = self.min_heap[0]

        if num < right:
            self.add_to_max_heap(num)
        else:
            self.add_to_min_heap(num)
        
    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 1:
            return -self.max_heap[0] if len(self.max_heap) > len(self.min_heap) else self.min_heap[0]
        
        return((-self.max_heap[0]) + self.min_heap[0]) / 2


class MedianFinder:

    def __init__(self):
        self.max_heap = [] # for the left side of the tree (smaller values)
        self.min_heap = [] # for the right side of the tree (larger values)
        self.median = None

    def add_to_max_heap(self, num): # first add and then pop
        heapq.heappush(self.max_heap, -num)

        if len(self.max_heap) > len(self.min_heap):
            larger_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, larger_num)
    
    def add_to_min_heap(self, num): # first pop and then add
        if len(self.min_heap) > len(self.max_heap):
            smaller_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -smaller_num)
        
        heapq.heappush(self.min_heap, num)

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            self.add_to_min_heap(num)
        else:
            self.add_to_max_heap(num)
        
    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 1:
            return -self.max_heap[0] if len(self.max_heap) > len(self.min_heap) else self.min_heap[0]
        
        return((-self.max_heap[0]) + self.min_heap[0]) / 2


class MedianFinder:

    def __init__(self):
        self.max_heap = [] # for the left side of the tree (smaller values)
        self.min_heap = [] # for the right side of the tree (larger values)
        self.median = None

    def add_to_max_heap(self, num): # first add and then pop
        heapq.heappush(self.max_heap, -num)

        if len(self.max_heap) > len(self.min_heap):
            larger_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, larger_num)
    
    def add_to_min_heap(self, num): # first add and then pop
        heapq.heappush(self.min_heap, num)

        if len(self.min_heap) > len(self.max_heap):
            smaller_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -smaller_num)

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            self.add_to_min_heap(num)
        else:
            self.add_to_max_heap(num)
        
    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 1:
            return -self.max_heap[0] if len(self.max_heap) > len(self.min_heap) else self.min_heap[0]
        
        return((-self.max_heap[0]) + self.min_heap[0]) / 2



class MedianFinder:

    def __init__(self):
        self.max_heap = [] # for the left side of the tree (smaller values)
        self.min_heap = [] # for the right side of the tree (larger values)
        self.median = None

    def balance(self):
        if len(self.min_heap) > len(self.max_heap):
            smaller_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -smaller_num)
        elif len(self.max_heap) > len(self.min_heap):
            larger_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, larger_num)

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        self.balance()
        
    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 1:
            return -self.max_heap[0] if len(self.max_heap) > len(self.min_heap) else self.min_heap[0]
        
        return((-self.max_heap[0]) + self.min_heap[0]) / 2