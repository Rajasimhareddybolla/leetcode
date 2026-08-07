class Twitter:

    def __init__(self):
        self.posts = [] # cronological reverse order 
        self.connections = {} # it will be follower : set(follower id ) 


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append((userId , tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []

        for infId , postId in reversed(self.posts):
            if infId in self.connections.get(userId , ()) or infId == userId:
                res.append(postId)
                if len(res) == 10:
                    break
        return res 
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.connections:
            self.connections[followerId] = set()
        self.connections[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.connections :
            self.connections[followerId].discard(followeeId)
