class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        width=j-i
        ans=min(height[i],height[j])*width
        while True:
            width-=1
            if width==0:
                return ans
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            ans=max(ans,min(height[i],height[j])*width)