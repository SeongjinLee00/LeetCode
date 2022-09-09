class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output=[]
        
        def backtrack(l, r, p):
            
            if l==n and r==n:
                output.append(p)
                return
            
            if l<n: backtrack(l+1,r,p+'(')
            if r<l: backtrack(l,r+1,p+')')
            
        backtrack(0,0,'')
        
        return output