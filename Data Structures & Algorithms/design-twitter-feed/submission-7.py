class Twitter:

    """
        1) Unfollow / Follow
            userId_a: set(userIds) (who follows userId_a)
                - O(1) operation to follow and unfollow users 

        2) Posting of Tweet:
            - number to trcak the "order" in which this tweet cam (some sort of global)
            - mapping: userId: [(order, tweetId)]
        
        3) Get News Feed:
            - grab all relevant tweets 
            - grab users tweets 
            - grab tweets of all users this user follows 
            - consturct a maxHeap (top 10 recent tweets === highest ordered tweets)

    """

    def __init__(self):
        self.following = {} # userId: set() 
        self.tweets = {} # userId: List
        self.order = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        # check if the user has posted before 
        if self.tweets and userId in self.tweets:
            self.tweets[userId].append((self.order, tweetId))
        else:
            self.tweets[userId] = [(self.order, tweetId)]
        
        # incremnet global order 
        self.order += 1 
        

    def getNewsFeed(self, userId: int) -> List[int]:

        # determine relevant users 
        users = [userId]
        if userId in self.following:
            for user in self.following[userId]:
                users.append(user)
        

        # grab relevant tweets and construct maxHeap 
        maxHeap = [] 
        
        # start with latest user tweets on heap 
        for user in users:
            
            user_tweets = self.tweets.get(user, [])
            if not user_tweets:
                continue

            order, tweetId = user_tweets[-1]
            idx = len(user_tweets) - 1

            heapq.heappush(maxHeap, (-order, tweetId, user, idx))
        

        # generate result 
        res = []

        while len(res) < 10 and maxHeap:

            # process latest tweet
            order, tweetId, userId, idx = heapq.heappop(maxHeap)
            res.append(tweetId)

            # add additional tweets for this user if necessary
            if idx >= 1:
                idx -= 1 
                order, tweetId = self.tweets[userId][idx]

                heapq.heappush(maxHeap, (-order, tweetId, userId, idx))
        
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        
        if self.following and followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = {followeeId}

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        
        if self.following and followerId in self.following:
            self.following[followerId].discard(followeeId)
            

        
