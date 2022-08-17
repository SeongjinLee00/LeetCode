class Solution:
    def longestPalindrome(self, s: str) -> str:
        N=len(s)
        
        dp=[[0]*N for _ in range(N)]
        
        tmp=[0,1]
        f=0
        for i in range(N):
            dp[i][i]=1
            if 0<=i+1<N and s[i]==s[i+1]:
                dp[i][i+1]=1
                if not f:
                    tmp=[i,i+2]
                    f=1

        for i in range(N-1, -1, -1):
            for j in range(i+1, N):
                if 0<=i+1<N and 0<=j-1<N and s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=1
                    if j-i+1>tmp[1]-tmp[0]:
                        tmp=[i,j+1]
        return s[tmp[0]:tmp[1]]