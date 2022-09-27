class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N=len(nums)
        now=0
        
        for i in range(N):
            if now<i:
                return False
            now=max(now,i+nums[i])

        return True