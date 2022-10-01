class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0]*len(s)
        
        if s[0]=='0':
            return 0
        if len(s)==1:
            return 1
        
        dp[0]=1*bool(1<=int(s[0])<=26)
        dp[1]=1*bool(1<=int(s[0]+s[1])<=26)+bool(1<=int(s[1])<=26)
        
        for i in range(2,len(s)):
            dp[i]=dp[i-2]*bool(s[i-1]!='0' and 1<=int(s[i-1]+s[i])<=26)+dp[i-1]*bool(1<=int(s[i])<=26)
        
        return dp[len(s)-1]