class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=list(s.split())
        
        d=dict()
        rd=set()
        if len(a)!=len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in d:
                if a[i]!=d[pattern[i]]:
                    return False
            else:
                if a[i] in rd:
                    return False
                d[pattern[i]]=a[i]
                rd.add(a[i])
        return True