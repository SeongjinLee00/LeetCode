class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        now=colors[0]
        
        group=[]
        ans=0
        for i in range(len(colors)):
            if colors[i]==now:
                group.append(neededTime[i])
            else:
                if len(group)>=2:
                    ans+=sum(group)
                    ans-=max(group)
                    now=colors[i]
                    group=[neededTime[i]]
                else:
                    now=colors[i]
                    group=[neededTime[i]]
        
        if len(group)>=2:
            ans+=sum(group)
            ans-=max(group)
        
        return ans