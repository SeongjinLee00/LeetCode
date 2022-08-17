class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret=""
        if len(s)==1:
            return s
        for i in range(len(s)):
            for j in range(len(s),i,-1):
                par=s[i:j]
                if len(par)>len(ret) and par==par[::-1]:
                    ret=par
        
        return ret