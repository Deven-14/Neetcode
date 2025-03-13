from collections import defaultdict, deque
from itertools import count
from operator import itemgetter
class Twitter:

    def __init__(self):
        deque10 = lambda: deque(maxlen=10)
        self.recent_tweets = defaultdict(deque10)
        self.followers = defaultdict(set)
        self.timestamp_counter = count()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.recent_tweets[userId].append((tweetId, next(self.timestamp_counter)))

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        max_heap.extend(self.recent_tweets[userId])

        for followeeId in self.followers[userId]:
            max_heap.extend(self.recent_tweets[followeeId])

        top10 = heapq.nlargest(10, max_heap, key=itemgetter(1))
        return [tweetId for tweetId, timestamp in top10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)


from collections import defaultdict, deque
from itertools import count
from operator import itemgetter
class Twitter:

    def __init__(self):
        deque10 = lambda: deque(maxlen=10)
        self.recent_tweets = defaultdict(deque10)
        self.followers = defaultdict(set)
        self.timestamp_counter = count()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.recent_tweets[userId].append((tweetId, next(self.timestamp_counter)))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        tweets.extend(self.recent_tweets[userId])

        for followeeId in self.followers[userId]:
            tweets.extend(self.recent_tweets[followeeId])

        top10 = heapq.nlargest(10, tweets, key=itemgetter(1))
        return [tweetId for tweetId, timestamp in top10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)


from collections import defaultdict, deque
from itertools import count
from operator import itemgetter
class Twitter:

    def __init__(self):
        deque10 = lambda: deque(maxlen=10)
        self.recent_tweets = defaultdict(deque10)
        self.followers = defaultdict(set)
        self.counter = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.recent_tweets[userId].append((self.counter, tweetId))
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        
        if self.recent_tweets[userId]:
            idx = len(self.recent_tweets[userId]) - 1
            count, tweetId = self.recent_tweets[userId][idx]
            max_heap.append((count, tweetId, userId, idx))
        
        for followeeId in self.followers[userId]:
            if self.recent_tweets[followeeId]:
                idx = len(self.recent_tweets[followeeId]) - 1
                count, tweetId = self.recent_tweets[followeeId][idx]
                max_heap.append((count, tweetId, followeeId, idx))
        
        heapq.heapify(max_heap)
        recent_10_tweets = []

        while max_heap and len(recent_10_tweets) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(max_heap)
            recent_10_tweets.append(tweetId)
            if idx - 1 >= 0:
                count, tweetId = self.recent_tweets[followeeId][idx - 1]
                heapq.heappush(max_heap, (count, tweetId, followeeId, idx - 1))

        return recent_10_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)

