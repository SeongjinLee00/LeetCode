class Solution:
    def countAndSay(self, n):
        if n==1: return("1")
        
        x = self.countAndSay(n-1)
        idx, res = 0, ""
        while(idx<len(x)):
            char = x[idx]
            nb = 0
            while(idx<len(x) and x[idx]==char):
                nb += 1
                idx += 1
            res += str(nb) + char
        return(res)