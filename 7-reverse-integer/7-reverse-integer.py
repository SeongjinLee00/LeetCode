class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            while not x%10:
                x//=10
            out=str(x)[::-1]
        elif x==0:
            out=0
        else:
            while not x%10:
                x//=10
            out='-'+str(x)[:0:-1]
        
        if -(2**31)<=int(out)<=(2**31)-1:
            return out
        else:
            return 0