class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        frequency = Counter(nums)
        ends = defaultdict(int)
        
        for n in nums:
            if frequency[n]==0:
                continue
                
            frequency[n]-=1
            
            if ends[n-1]>0:
                ends[n-1]-=1
                ends[n]+=1
            
            elif frequency[n+1] and frequency[n+2]:
                ends[n+2]+=1
                frequency[n+1]-=1
                frequency[n+2]-=1
            
            else:
                return False
        
        return True