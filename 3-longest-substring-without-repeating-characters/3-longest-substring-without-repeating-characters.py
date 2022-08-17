class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        i=0
        j=0
        
        ret=1
        tmp=1
        used=set(s[0])
        
        while True:
            if j==len(s)-1:
                return ret
            if s[j+1] not in used:
                j+=1
                used.add(s[j])
                tmp+=1
                ret=max(tmp,ret)
            else:
                used.remove(s[i])
                i+=1
                tmp-=1