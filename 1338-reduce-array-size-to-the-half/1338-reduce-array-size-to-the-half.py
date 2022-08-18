class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        tmp=[0]*(10**5+1)
        for i in arr:
            tmp[i]+=1
        tmp.sort()
        
        N=len(arr)
        s=0
        
        ret=0
        while s<N//2:
            s+=tmp.pop()
            ret+=1
        return ret