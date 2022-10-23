class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        a=0
        b=0
        for k,v in c.items():
            if v==2:
                a=k
        for i in range(1,len(nums)+1):
            if i not in c:
                b=i
                break
        return [a,b]