class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        d=defaultdict(list)
        
        for num in nums:
            d[num%space].append(num)
        
        m=-1
        mval=-1
        mk=-1
        for k,v in d.items():
            if len(v)>m or (len(v)==m and min(v)<mval):
                mk=k
                mval=min(v)
                m=len(v)
        
        return min(d[mk])