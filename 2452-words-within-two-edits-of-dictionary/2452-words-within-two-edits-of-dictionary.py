class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        N=len(queries[0])
        
        ret=[]
        
        for word1 in queries:
            for word2 in dictionary:
                difference=0
                
                for i in range(N):
                    if word1[i]!=word2[i]:
                        difference+=1
                
                if difference<=2:
                    ret.append(word1)
                    break
        
        return ret