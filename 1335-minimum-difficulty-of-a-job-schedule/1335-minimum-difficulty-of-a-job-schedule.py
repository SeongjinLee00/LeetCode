class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        N = len(A)  
		
		# i current job
		# b value of job before
		# d days left
        @cache
        def dp(i,b,d):
            # we couldn't use all the days
            if i == N and d > 0: return inf
            
            # no days and no jobs
            if i == N and d == 0: return b
            
            # no days but we have jobs
            if d == 0: return dp(i+1,max(b,A[i]),d)
            
            
            # 2 options 
            # s1 - stop and start new day
            # s2 - keep moving
            s1 = b + dp(i+1,A[i],d-1)
            s2 = dp(i+1,max(A[i],b),d)
            
            return min(s1,s2)
        
        ans = dp(1,A[0],d-1)
        
        return -1 if ans == inf else ans