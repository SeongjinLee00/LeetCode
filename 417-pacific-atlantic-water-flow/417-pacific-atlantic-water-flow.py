class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        N=len(heights)
        M=len(heights[0])
        
        dr=[1,-1,0,0]
        dc=[0,0,1,-1]
        
        pacific=[[0]*M for _ in range(N)]
        atlantic=[[0]*M for _ in range(N)]
        
        def bfs(i,j,PA):
            q=deque([[i,j]])
            visited=[[0]*M for _ in range(N)]
            visited[i][j]=1
            if PA:
                pacific[i][j]=1
            else:
                atlantic[i][j]=1
            while q:
                r,c=q.popleft()
                H=heights[r][c]
                for k in range(4):
                    rr=r+dr[k]
                    cc=c+dc[k]
                    if 0<=rr<N and 0<=cc<M and not visited[rr][cc] and heights[rr][cc]>=H:
                        q.append([rr,cc])
                        visited[rr][cc]=1
                        if PA:
                            pacific[rr][cc]=1
                        else:
                            atlantic[rr][cc]=1
        
        for i in range(N):
            for j in range(M):
                if (i==0 or j==0) and not pacific[i][j]:
                    bfs(i,j,1)
                if (i==N-1 or j==M-1) and not atlantic[i][j]:
                    bfs(i,j,0)
        output=[]
        for i in range(N):
            for j in range(M):
                if atlantic[i][j] and pacific[i][j]:
                    output.append([i,j])
                    
        return output