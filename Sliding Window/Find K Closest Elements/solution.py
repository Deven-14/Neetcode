from bisect import bisect_left
from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)
        n = len(arr)
        result = deque()

        l, r = idx-1, idx
        while k:
            if l >= 0 and r < n:
                if (x - arr[l]) <= (arr[r] - x):
                    result.appendleft(arr[l])
                    l -= 1
                else:
                    result.append(arr[r])
                    r += 1
            elif l >= 0:
                result.appendleft(arr[l])
                l -= 1
            else:
                result.append(arr[r])
                r += 1
            
            k -= 1
        
        return list(result)



from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)
        n = len(arr)

        l, r = idx-1, idx
        while k:
            if l < 0:
                r += 1
            elif r >= n:
                l -= 1
            elif (x - arr[l]) <= (arr[r] - x):
                l -= 1
            else:
                r += 1
            
            k -= 1
        
        return arr[l + 1:r]



from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        
        return arr[l:l + k]