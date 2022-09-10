class Solution:
    def mySqrt(self, x: int) -> int:
        r=1000000
        dr=1000000
        iteration=0
        
        if x==0:
            return 0
        
        while iteration<1000:
            if r*r<x:
                r+=dr
            else:
                r-=dr
            dr/=2
            iteration+=1
        
        if r%1>0.999999:
            return int(r)+1
        else:
            return int(r)