class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.order = 1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.order, tweetId))
        self.order += 1 
        

    def getNewsFeed(self, userId: int) -> List[int]:

        # construct max heap 
        users = self.following[userId]
        users.add(userId)

        # construct max heap with "latest" tweets from each relevant user 
        maxHeap = [] 
        for userId in users:

            # ensure user has relevant tweets prior to processing
            if not self.tweets[userId]:
                continue 

            # grab latest tweet for user 
            order, tweetId = self.tweets[userId][-1]

            # grab current index that we added 
            idx = len(self.tweets[userId]) - 1

            # add latest tweet to maxHeap 
            heapq.heappush(maxHeap, (-order, idx, userId, tweetId))
        

        # construct result while heap has elements and we are under 10 
        count = 0 
        result = [] 
        while count < 10 and maxHeap: 

            # grab latest tweet from heap
            order, idx, userId, tweetId = heapq.heappop(maxHeap)

            # add tweetId to result 
            result.append(tweetId)

            # check if any other tweets corresponding to user to add to heap (if applicable) 
            if idx == 0:
                count += 1 
                continue 
            
            # grab next tweet relevant to user 
            next_order, next_tweet_id = self.tweets[userId][idx - 1]

            # add to heap 
            heapq.heappush(maxHeap, (-next_order, idx - 1, userId, next_tweet_id))

            count += 1 
        

        return result



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
