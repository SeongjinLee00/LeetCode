class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        def dp(s,i):
            if s==target and i==n:
                return 1
            elif s>target or i>n:
                return 0
            elif (s,i) in memo:
                return memo[(s,i)]
            else:
                ways = 0
                for j in range(1,k+1):
                    ways+=dp(s+j,i+1)
                memo[(s,i)] = ways%1000000007
                return memo[(s,i)]
        
        return dp(0,0)