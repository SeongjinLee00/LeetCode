class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer=[[0]*n for _ in range(n)]
        
        cnt=1
        
        i=0
        j=0
        
        answer[i][j]=cnt
        while True:
            while j<n-1 and not answer[i][j+1]:
                j+=1
                cnt+=1
                answer[i][j]=cnt
            
            while i<n-1 and not answer[i+1][j]:
                i+=1
                cnt+=1
                answer[i][j]=cnt
        
            while j>0 and not answer[i][j-1]:
                j-=1
                cnt+=1
                answer[i][j]=cnt
            
            while i>0 and not answer[i-1][j]:
                i-=1
                cnt+=1
                answer[i][j]=cnt
            
            if cnt==n*n:
                return answer