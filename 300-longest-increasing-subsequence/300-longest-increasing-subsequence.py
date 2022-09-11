class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack=[nums[0]]
        
        for num in nums:
            if num>stack[-1]:
                stack.append(num)
            else:
                stack[bisect_left(stack,num)]=num
        
        return len(stack)