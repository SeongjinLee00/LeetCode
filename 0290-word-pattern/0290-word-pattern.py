class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        
        if len(pattern)!=len(s):
            return False
        
        d=dict()
        used=set()
        
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if s[i] in used:
                    return False
                d[pattern[i]]=s[i]
                used.add(s[i])
            elif d[pattern[i]]!=s[i]:
                return False
        
        return True