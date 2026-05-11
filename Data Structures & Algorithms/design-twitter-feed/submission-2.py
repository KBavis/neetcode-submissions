

class Twitter:

    def __init__(self):
        self.time = 0 
        self.tweets = defaultdict(list) #userId: []
        self.following = defaultdict(set) #userId: set() 
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        result = [] 
        maxHeap = [] 

        users = self.following[userId] | {userId} # union users followed by user with user 
        
        # initalize heap
        for u in users:
            
            # if user has tweets, add LATEST tweet to maxHeap
            if self.tweets[u]:
                index = len(self.tweets[u]) - 1
                tweet_time, tweetId = self.tweets[u][index]
                
                heapq.heappush(maxHeap, (-tweet_time, tweetId, index, u)) # negate time in order to construct maxHeap 

        

        # construct result 
        while maxHeap and len(result) < 10:

            # pop of most recent tweet 
            neg_time, tweetId, idx, userId = heapq.heappop(maxHeap)

            # add to result 
            result.append(tweetId)

            # add users next tweet if possible 
            if idx != 0:
                idx -= 1 
                tweet_time, tweetId = self.tweets[userId][idx]
                heapq.heappush(maxHeap, (-tweet_time, tweetId, idx, userId))
        

        return result 
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
 
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

        
