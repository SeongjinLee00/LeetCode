class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        s=set()
        for i in range(33):
            s.add(2**i)
        
        if n in s:
            return True
        return False