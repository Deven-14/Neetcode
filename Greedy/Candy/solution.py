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

        
