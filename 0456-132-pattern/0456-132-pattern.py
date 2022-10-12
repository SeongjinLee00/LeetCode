class Solution:
    def find132pattern(self, nums):
        mid = -float('inf')
        stack = []
        for num in nums[::-1]:
            if(num < mid):
                return 1
            while(stack and stack[-1] < num):
                mid = stack.pop()
            stack.append(num)
        return 0