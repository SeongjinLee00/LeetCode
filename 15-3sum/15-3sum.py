class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret=set()
        
        nums.sort()

        def twoPointerSearch(k):
            i=0
            j=len(nums)-1
            
            third=nums[k]
            while True:
                if nums[i]+nums[j]+third>0:
                    j-=1
                elif nums[i]+nums[j]+third<0:
                    i+=1
                else:

                    ret.add((nums[i],third,nums[j]))
                    j-=1
                
                if i==j or i==k or j==k: return
        
        for k in range(1,len(nums)-1):

            twoPointerSearch(k)

        return list(ret)