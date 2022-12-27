class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        pq=[]
        
        ans=0
        
        for i in range(len(capacity)):
            if capacity[i]==rocks[i]:
                ans+=1
            else:
                heappush(pq,capacity[i]-rocks[i])
        
        while pq and additionalRocks:
            now=heappop(pq)
            
            if now<=additionalRocks:
                additionalRocks-=now
                ans+=1
            else:
                break
        
        return ans