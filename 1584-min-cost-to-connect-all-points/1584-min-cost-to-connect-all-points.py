class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents=[i for i in range(len(points))]
        def union(x,y):
            a=find(x)
            b=find(y)
            parents[max(a,b)]=min(a,b)
        
        def find(x):
            if parents[x]!=x:
                parents[x]=find(parents[x])
            
            return parents[x]
        
        lines=[]
        
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                distance=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                lines.append([i,j,distance])
        
        lines.sort(key=lambda x:x[2])
        
        ans=0
        for start,end,cost in lines:
            if find(start)!=find(end):
                ans+=cost
                union(start,end)
                
        return ans