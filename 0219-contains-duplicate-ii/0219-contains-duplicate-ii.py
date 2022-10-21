class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d=defaultdict(int)
        
        for i in range(len(nums)):
            if d[nums[i]] and d[nums[i]]>=i+1-k:
                return True
            d[nums[i]]=i+1
        
        return False