class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        q=deque()
        for i in range(len(nums)):
            q.append([[nums[i]],i])
        
        visited=[0]*len(nums)
        
        ans=-1
        ret=[]
        while q:
            path,idx=q.popleft()
            if len(path)>ans:
                ans=len(path)
                ret=path
            
            if visited[idx]>=len(path):
                continue
                
            visited[idx]=len(path)
            
            for next in range(idx+1,len(nums)):
                if nums[next]%path[-1]==0:
                    q.append([path+[nums[next]],next])
        
        return ret