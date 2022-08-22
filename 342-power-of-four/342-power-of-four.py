class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        s=set()
        for i in range(63):
            s.add(4**i)
        
        if n in s:
            return True
        return False