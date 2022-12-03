# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        lo=-1
        hi=n+1
        
        while True:
            mid=(lo+hi)//2
            
            if isBadVersion(mid):
                hi=mid
            else:
                lo=mid
                
            if lo+1==hi:
                return hi