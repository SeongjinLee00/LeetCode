class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0
        visited=[[0]*len(grid[0]) for _ in range(len(grid))]
        def bfs(r,c):
            dr=[1,-1,0,0]
            dc=[0,0,1,-1]
            area=1
            q=deque([[r,c]])
            visited[r][c]=1
            
            while q:
                r,c=q.popleft()
                for i in range(4):
                    rr=r+dr[i]
                    cc=c+dc[i]
                    if 0<=rr<len(grid) and 0<=cc<len(grid[0]) and not visited[rr][cc] and grid[rr][cc]:
                        q.append([rr,cc])
                        visited[rr][cc]=1
                        area+=1
            
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]:
                    ans=max(ans,bfs(i,j))
        
        return ans