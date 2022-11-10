class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        
        for c in s:
            if not stack:
                stack.append([c,1])
            else:
                if stack[-1][0]==c:
                    if stack[-1][1]==k-1:
                        stack.pop()
                    else:
                        stack[-1][1]+=1
                else:
                    stack.append([c,1])
        
        ans=''
        for c, d in stack:
            ans+=c*d
        
        return ans