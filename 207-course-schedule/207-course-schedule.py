class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        graph=[[] for _ in range(numCourses)]
        
        for e,s in prerequisites:
            indegree[e]+=1
            graph[s].append(e)
        
        q=deque()
        
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            now=q.popleft()
            for next in graph[now]:
                indegree[next]-=1
                if indegree[next]==0:
                    q.append(next)
        
        return not sum(indegree)