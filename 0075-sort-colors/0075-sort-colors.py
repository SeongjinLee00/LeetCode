class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnts=[0]*3
        
        for num in nums:
            cnts[num]+=1
        
        print(cnts)
        
        for i in range(cnts[0]):
            nums[i]=0
        for j in range(cnts[0],cnts[0]+cnts[1]):
            nums[j]=1
        for k in range(cnts[0]+cnts[1],cnts[0]+cnts[1]+cnts[2]):
            nums[k]=2