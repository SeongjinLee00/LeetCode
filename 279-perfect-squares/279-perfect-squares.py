class Solution:
    def numSquares(self, n: int) -> int:
        q=deque([[0,0]])
        visited=[0]*(n+1)
        
        while q:
            s, d = q.popleft()
            if s==n:
                return d
            for i in range(1,int((n-s)**0.5)+1):
                if not visited[s+i*i]:
                    q.append([s+i*i,d+1])
                    visited[s+i*i]=1