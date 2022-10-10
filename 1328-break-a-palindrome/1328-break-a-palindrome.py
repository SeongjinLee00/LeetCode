class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome=list(palindrome)
        
        for i in range(len(palindrome)):
            if palindrome[i]!='a':
                if i==len(palindrome)//2 and len(palindrome)%2:
                    continue
                palindrome[i]='a'
                
                return "".join(palindrome)
        
        if len(palindrome)>=2:
            palindrome.pop()
            return "".join(palindrome)+'b'
        return ""