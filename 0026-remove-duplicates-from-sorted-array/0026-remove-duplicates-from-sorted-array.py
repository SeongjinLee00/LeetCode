class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt=0
        tmp=-101
        
        for i in range(len(nums)):
            if nums[i]!=tmp:
                tmp=nums[i]
                nums[cnt]=tmp
                cnt+=1
        return cnt