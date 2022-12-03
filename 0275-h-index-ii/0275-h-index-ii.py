class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lo=0
        hi=len(citations)-1
        
        if len(citations)==1:
            return min(citations[0],1)

        while True:
            mid=(lo+hi)//2
            
            if citations[mid]>=len(citations)-mid:
                hi=mid
            else:
                lo=mid
            
            if lo+1>=hi:
                if citations[lo]>=len(citations)-lo:
                    return len(citations)-lo
                elif citations[hi]<len(citations)-hi:
                    return len(citations)-hi-1
                else:
                    return len(citations)-hi