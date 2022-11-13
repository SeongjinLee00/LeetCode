class Solution:
    def reverseWords(self, s: str) -> str:
        t=s.strip().split()
        
        return " ".join(t[::-1])