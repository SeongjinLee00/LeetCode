class Solution:
    def trap(self, height: List[int]) -> int:
        N=len(height)
        
        left=[0]*N
        right=[0]*N
        
        M=0
        for i in range(N):
            if height[i]>M:
                M=height[i]
            left[i]=M
        M=0
        for i in range(N-1,-1,-1):
            if height[i]>M:
                M=height[i]
            right[i]=M
        
        ans=0
        
        for i in range(N):
            ans+=height[i]-min(left[i],right[i])
        
        return -ans