class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph=[[] for _ in range(n)]
        
        for s,e in dislikes:
            graph[s-1].append(e-1)
            graph[e-1].append(s-1)
            
        red=set()
        black=set()
        visited=set()

        def bfs(now):
            q=deque([[now,0]])
            visited.add(now)
            while q:
                now, color = q.popleft()

                if color==0:
                    red.add(now)
                elif color==1:
                    black.add(now)

                for next in graph[now]:
                    if (color==0 and next in red) or (color==1 and next in black):
                        return False
                    if next not in visited:
                        q.append([next,-color+1])
                        visited.add(next)
            return True
        
        for i in range(n):
            if i not in visited:
                if not bfs(i):
                    return False

        return True