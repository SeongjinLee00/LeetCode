class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans=[]
        
        def backtrack(cnt,num,last):

            if cnt==n:
                ans.append(num)
                return
            
            if 0<=last+k<=9: backtrack(cnt+1,num*10+last+k,last+k)
            if k!=0 and 0<=last-k<=9: backtrack(cnt+1,num*10+last-k,last-k)
                
        backtrack(1,1,1)
        backtrack(1,2,2)
        backtrack(1,3,3)
        backtrack(1,4,4)
        backtrack(1,5,5)
        backtrack(1,6,6)
        backtrack(1,7,7)
        backtrack(1,8,8)
        backtrack(1,9,9)
        
        return ans