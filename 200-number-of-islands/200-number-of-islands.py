class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ans=0
        visited=[[0]*len(grid[0]) for _ in range(len(grid))]
        def bfs(r,c):
            dr=[1,-1,0,0]
            dc=[0,0,1,-1]
            q=deque([[r,c]])
            visited[r][c]=1
            
            while q:
                r,c=q.popleft()
                for i in range(4):
                    rr=r+dr[i]
                    cc=c+dc[i]
                    if 0<=rr<len(grid) and 0<=cc<len(grid[0]) and not visited[rr][cc] and grid[rr][cc]=="1":
                        q.append([rr,cc])
                        visited[rr][cc]=1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]=="1":
                    ans+=1
                    bfs(i,j)
        
        return ans