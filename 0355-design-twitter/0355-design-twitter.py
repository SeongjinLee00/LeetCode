class Twitter:

    def __init__(self):
        self.article=defaultdict(list)
        self.follows=defaultdict(set)
        self.time=0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.article[userId].append([tweetId,self.time])
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        tmp=[]
        tmp+=self.article[userId]
        for following in self.follows[userId]:
            tmp+=self.article[following]
            
        tmp.sort(key=lambda x:-x[1])
        
        ret=[]
        cnt=0
        for item in tmp:
            ret.append(item[0])
            cnt+=1
            if cnt==10:
                break
        
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return
        self.follows[followerId].remove(followeeId)        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)