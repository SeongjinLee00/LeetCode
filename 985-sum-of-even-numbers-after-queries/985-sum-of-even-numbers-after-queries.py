class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        
        e=0
        for num in nums:
            if not num%2:
                e+=num
                
        for a,i in queries:
            if a%2:
                if nums[i]%2:
                    e+=(nums[i]+a)
                else:
                    e-=nums[i]
            else:
                if not nums[i]%2:
                    e+=a
            nums[i]+=a
            ans.append(e)
        
        return ans