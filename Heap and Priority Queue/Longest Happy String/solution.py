class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = [""]
        fs = ""

        def dfs(a, b, c, s):
            nonlocal fs
            if len(s) > len(fs):
                fs = "".join(s)            
            
            prev = s[-1]
            if a > 0 and prev != 'a':
                s.append('a')
                dfs(a-1, b, c, s)
                s.pop()
            
            if a-1 > 0 and prev != 'a':
                s.append('a')
                s.append('a')
                dfs(a-2, b, c, s)
                s.pop()
                s.pop()
            
            if b > 0 and prev != 'b':
                s.append('b')
                dfs(a, b-1, c, s)
                s.pop()
            
            if b-1 > 0 and prev != 'b':
                s.append('b')
                s.append('b')
                dfs(a, b-2, c, s)
                s.pop()
                s.pop()

            if c > 0 and prev != 'c':
                s.append('c')
                dfs(a, b, c-1, s)
                s.pop()
            
            if c-1 > 0 and prev != 'c':
                s.append('c')
                s.append('c')
                dfs(a, b, c-2, s)
                s.pop()
                s.pop()

        dfs(a, b, c, s)
        
        return fs
    
# ! time limit exceeded


import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if (a + b + c) < 3:
            return 'a' * a + 'b' * b + 'c' * c

        max_heap = []
        if a > 0:
            max_heap.append((-a, 'a'))
        if b > 0:
            max_heap.append((-b, 'b'))
        if c > 0:
            max_heap.append((-c, 'c'))
        heapq.heapify(max_heap)
        res = []
        
        for _ in range(2):
            count, char = heapq.heappop(max_heap)
            res.append(char)
            count += 1
            if count != 0:
                heapq.heappush(max_heap, (count, char))
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            if res[-1] == res[-2] == char:
                if not max_heap:
                    break
                
                count2, char2 = heapq.heappop(max_heap)
                res.append(char2)
                count2 += 1
                if count2 != 0:
                    heapq.heappush(max_heap, (count2, char2))
                heapq.heappush(max_heap, (count, char))
            
            else:
                res.append(char)
                count += 1
                if count != 0:
                    heapq.heappush(max_heap, (count, char))
                        
        return "".join(res)
