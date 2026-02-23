from collections import deque
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        min_rating = min(ratings)
        queue = deque((i, 1) for i, rating in enumerate(ratings) if rating == min_rating)
        candies = [0] * n

        while queue:
            idx, ncandies = queue.popleft()
            if ncandies <= candies[idx]:
                continue
            
            candies[idx] = ncandies
            if idx-1 >= 0:
                queue.append((idx-1, ncandies + 1 if ratings[idx-1] > ratings[idx] else 1))
            
            if idx+1 < n:
                queue.append((idx+1, ncandies + 1 if ratings[idx+1] > ratings[idx] else 1))

        return sum(candies)

        
from collections import deque
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)


from collections import deque
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = n
        i = 1

        while i < n:
            if ratings[i] == ratings[i - 1]:
                i += 1
                continue

            inc = 0
            while i < n and ratings[i] > ratings[i - 1]:
                inc += 1
                res += inc
                i += 1
        
            dec = 0
            while i < n and ratings[i] < ratings[i - 1]:
                dec += 1
                res += dec
                i += 1
            
            res -= min(inc, dec)
        
        return res