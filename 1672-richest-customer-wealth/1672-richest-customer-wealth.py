class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=0
        for item in accounts:
            ans=max(sum(item), ans)
        
        return ans