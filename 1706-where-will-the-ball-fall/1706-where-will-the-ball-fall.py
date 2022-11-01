class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        R=len(grid)
        C=len(grid[0])
        
#         if R==1 and C==1:
#             return [-1]
        
#         answer=[0]*C
        
#         if R==1:
#             for c in range(C):
#                 if grid[0][c]==1 and c<C-1 and grid[0][c+1]==1:
#                     answer[c]=c+1
#                 elif grid[0][c]==-1 and c>0 and grid[0][c-1]==-1:
#                     answer[c]=c-1
#                 else:
#                     answer[c]=-1
        
#             return answer
        
        def dfs(r,c):
            if r==R-1:
                if grid[r][c]==1 and c<C-1 and grid[r][c+1]==1:
                    return c+1
                elif grid[r][c]==-1 and c>0 and grid[r][c-1]==-1:
                    return c-1
                else:
                    return -1
                
            
            if grid[r][c]==1:
                if c==C-1:
                    return -1
                if grid[r][c+1]==1:
                    return dfs(r+1,c+1)
            
            if grid[r][c]==-1:
                if c==0:
                    return -1
                if grid[r][c-1]==-1:
                    return dfs(r+1,c-1)
            
            return -1
        
        answer=[0]*C
        
        for c in range(C):
            answer[c]=dfs(0,c)
            
        return answer