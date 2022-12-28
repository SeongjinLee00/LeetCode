class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq=[]
        
        for num in piles:
            heappush(pq,-num)
            
        for _ in range(k):
            heappush(pq,-ceil(-heappop(pq)/2))
        
        return -sum(pq)