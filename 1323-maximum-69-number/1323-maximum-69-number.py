class Solution:
    def maximum69Number (self, num: int) -> int:
        ans=''
        flag=0
        for c in str(num):
            if c=='6' and not flag:
                ans+='9'
                flag=1
            else:
                ans+=c
        
        return ans