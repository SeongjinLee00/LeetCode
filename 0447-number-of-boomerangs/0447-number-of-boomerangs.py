class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans=0
        for i in range(len(points)):
            distances=defaultdict(int)
            for j in range(len(points)):
                if i==j:
                    continue
                
                x1,y1=points[i]
                x2,y2=points[j]
                
                distance=((x2-x1)**2+(y2-y1)**2)**0.5
                distances[distance]+=1
            
            for num in distances.values():
                ans+=num*(num-1)
        
        return ans