class Solution:
    def canJump(self, nums: List[int]) -> bool:
        now=0
        N=len(nums)
        for i in range(N):
            if now<i:
                return False
            now=max(now,i+nums[i])

        return True