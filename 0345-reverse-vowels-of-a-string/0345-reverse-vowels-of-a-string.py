class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        
        arr=[]
        
        for c in s:
            if c in vowels:
                arr.append(c)
        
        ans=''
        
        for c in s:
            if c in vowels:
                ans+=arr.pop()
            else:
                ans+=c
                
        return ans