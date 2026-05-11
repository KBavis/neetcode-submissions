class Twitter:
    """
    1. use a set for who a user follows:
        user: [whoUserFollows1, whoUserFollows2]

    2. in general, we keep track of "time" as a global 
            - each new tweet increments our global time 
    
    3. use a mapping of a user: [postedTweets]

    4. the easiest way to implement get news feed is to always find most recent tweet off all possible tweets 
    """

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1 # decrement time since we want a max heap 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        user_ids = self.following[userId] 
        user_ids.add(userId)

        # init max heap with latst tweets from each user
        max_heap = [] 
        for user_id in user_ids:
            
            tweets = self.tweets[user_id]
            if not tweets:
                continue # skip if user has no tweets 
            
            idx = len(tweets) - 1
            time, tweetId = tweets[idx]
            heapq.heappush(max_heap, (time, tweetId, user_id, idx))
        

        res = []
        count = 0
        while max_heap and count < 10:

            time, tweetId, user_id, idx = heapq.heappop(max_heap)
            res.append(tweetId)

            # add next tweet to heap if applicable 
            if idx - 1 >= 0:
                next_tweet_time, next_tweet_id = self.tweets[user_id][idx - 1]
                heapq.heappush(max_heap, (next_tweet_time, next_tweet_id, user_id, idx - 1))
            
            count +=1
        

        return res 


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
