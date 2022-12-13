class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp=[[0]*len(matrix) for _ in range(len(matrix[0]))]

        dp[0]=matrix[0]

        print(dp)

        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if j==0:
                    dp[i][j]=matrix[i][j]+min(dp[i-1][j],dp[i-1][j+1])
                elif j==len(matrix[0])-1:
                    dp[i][j]=matrix[i][j]+min(dp[i-1][j-1],dp[i-1][j])
                else:
                    dp[i][j]=matrix[i][j]+min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
        
        return min(dp[len(matrix)-1])