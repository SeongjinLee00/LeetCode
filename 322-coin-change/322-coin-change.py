class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        s=set()
        
        q=deque([[0,0]])
        
        while q:
            d,c=q.popleft()
            if c==amount:
                return d
            
            for a in coins:
                if c+a<=amount and c+a not in s:
                    q.append([d+1,c+a])
                    s.add(c+a)
        
        return -1