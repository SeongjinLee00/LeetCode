class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ret=[]
        
        m,n=len(nums1),len(nums2)
        
        pq=[[nums1[0]+nums2[0],0,0]]
        
        visited={(0,0)}
        
        target=min(k,m*n)
        
        cnt=0
        
        while pq:
            now,i,j=heappop(pq)
            
            ret.append([nums1[i],nums2[j]])
            
            cnt+=1
            if cnt==target:
                return ret
            
            if (i+1,j) not in visited and i+1<m:
                heappush(pq,[nums1[i+1]+nums2[j],i+1,j])
                visited.add((i+1,j))
            if (i,j+1) not in visited and j+1<n:
                heappush(pq,[nums1[i]+nums2[j+1],i,j+1])
                visited.add((i,j+1))