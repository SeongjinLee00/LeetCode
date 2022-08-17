class Solution:
    def twoSum(self, nums, target):
        nums2=sorted(nums)
        
        i=0
        j=len(nums2)-1
        while True:
            if nums2[i]+nums2[j]<target:
                i+=1
            elif nums2[i]+nums2[j]>target:
                j-=1
            else:
                ret=[]
                flag=0
                for k in range(len(nums)):

                    if flag and (nums[k]==nums2[i] or nums[k]==nums2[j]):
                        ret.append(k)
                        return ret
                    if (nums[k]==nums2[i] or nums[k]==nums2[j]):
                        ret.append(k)
                        flag=1