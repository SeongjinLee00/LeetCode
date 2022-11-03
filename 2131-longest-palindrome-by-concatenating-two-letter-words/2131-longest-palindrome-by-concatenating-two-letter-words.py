class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        different=defaultdict(lambda:[0,0])
        same=defaultdict(int)
        
        for word in words:
            if word[0]==word[1]:
                same[word]+=1
            else:
                if word[0]>word[1]:
                    different[word[1]+word[0]][1]+=1
                else:
                    different[word][0]+=1
        
        ans=0
        
        for v in different.values():
            ans+=(min(v[0],v[1])*2)
        
        oddmax=0
        odds=[]
        for v in same.values():
            if v%2:
                oddmax=max(oddmax,v)
                odds.append(v)
            else:
                ans+=v
        
        if len(odds)>=2:
            ans+=sum(odds)-len(odds)+1
        else:
            ans+=oddmax

        return ans*2