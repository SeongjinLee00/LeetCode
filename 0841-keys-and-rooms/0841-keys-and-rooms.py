class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q=deque([0])
        visited=set([0])
        
        while q:
            now=q.popleft()
            for next in rooms[now]:
                if next not in visited:
                    q.append(next)
                    visited.add(next)
        print(visited)
        return len(visited)==len(rooms)