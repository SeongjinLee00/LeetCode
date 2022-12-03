class Solution:
    def frequencySort(self, s: str) -> str:
        d=defaultdict(int)
        
        for c in s:
            d[c]+=1
        
        ans=''
        for k,v in sorted(d.items(), key=lambda x:-x[1]):
            ans+=k*v
        
        return ans