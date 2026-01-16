from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_heap = [(-count, ele) for ele, count in counts.items()]
        new_s = []

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            fc, fele = heapq.heappop(max_heap)
            sc, sele = heapq.heappop(max_heap)
            new_s.append(fele)
            new_s.append(sele)
            if fc + 1 < 0:
                heapq.heappush(max_heap, (fc + 1, fele))
            if sc + 1 < 0:
                heapq.heappush(max_heap, (sc + 1, sele))
        
        if max_heap:
            c, ele = max_heap[0]
            c = -c
            if c > 1:
                return ""
            
            new_s.append(ele)
        
        return "".join(new_s)
