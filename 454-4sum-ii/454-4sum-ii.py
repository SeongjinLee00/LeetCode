class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d=defaultdict(int)
        
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                d[nums3[k]+nums4[l]]+=1
        
        ans=0
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                ans+=d[-nums1[i]-nums2[j]]
        
        return ans