class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        q=deque([source])
        
        graph=[[] for _ in range(n)]
        visited=[0]*n
        
        visited[source]=1
        
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)
            
        while q:
            now=q.popleft()
            if now==destination:
                return True
            for next in graph[now]:
                if not visited[next]:
                    q.append(next)
                    visited[next]=1
                    
        return False