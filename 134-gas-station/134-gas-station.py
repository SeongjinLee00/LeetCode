class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        N=len(gas)
        
        ans=0
        tank=0
        for i in range(N):
            tank+=(gas[i]-cost[i])
            
            if tank<0:
                ans=i+1
                tank=0
        
        return ans