class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R=len(grid)
        C=len(grid[0])
        
        dp=[[0]*C for _ in range(R)]
        dp[0][0]=grid[0][0]
        
        for c in range(1,C):
            dp[0][c]=dp[0][c-1]+grid[0][c]
        for r in range(1,R):
            dp[r][0]=dp[r-1][0]+grid[r][0]
        
        for i in range(1,R):
            for j in range(1,C):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
                
        return dp[R-1][C-1]