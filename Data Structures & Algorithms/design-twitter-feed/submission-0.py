import heapq

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = {} # key as user Id, value as tweets array
        self.following = {} # key as user Id who follows the other users which is stored as values in set
        self.limit = 10

    def postTweet(self, userId: int, tweetId: int) -> None: # O(1)
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.count += 1
        self.tweets[userId].append((tweetId, self.count))


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            self.following[userId] = set()
        
        users = list(self.following[userId])
        users.append(userId)
        news_feed = []
        for user in users:
            if user not in self.tweets:
                self.tweets[user] = []
            
            for tweet_id, count in self.tweets[user][-self.limit:]:
                heapq.heappush(news_feed, (count, tweet_id))
                if len(news_feed) > self.limit:
                    heapq.heappop(news_feed)
        
        result = []
        while news_feed:
            _, tweet_id = heapq.heappop(news_feed)
            result.append(tweet_id)
        return result[::-1]
        
        

    def follow(self, followerId: int, followeeId: int) -> None: # O(1)
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None: # O(1)
        if followerId not in self.following:
            return
        self.following[followerId].discard(followeeId)