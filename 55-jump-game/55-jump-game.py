class Solution:
    def canJump(self, nums: List[int]) -> bool:
        now=0

        for i in range(len(nums)):
            if now<i:
                return False
            now=max(now,i+nums[i])

        return True