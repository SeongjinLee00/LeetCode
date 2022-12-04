class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        ans=9999999
        ret=-1
        
        now=0
        rest=sum(nums)
        for i in range(len(nums)):
            now+=nums[i]
            rest-=nums[i]
            
            if len(nums)-i-1==0:
                average_difference=(now//(i+1))
            else:
                average_difference=abs((now//(i+1))-(rest//(len(nums)-i-1)))

            if average_difference<ans:
                ans=average_difference
                ret=i
        
        return ret