import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(point):
            x, y = point
            return math.sqrt(abs(x * x) + abs(y * y)) # as the other point is [0, 0]

        return heapq.nsmallest(k, points, distance)
    
# time complexity: O(nlogk)
# space complexity: O(k)

# * we can do this using quick select / sort algorithm as well, 
# * the trick is to do the partitioning only on the smaller side until the smaller side is equal to k
# time complexity: O(n) on average, O(n^2) in worst case
# space complexity O(1)