class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        s=set()
        for i in range(30):
            s.add(3**i)
        
        if n in s:
            return True
        return False