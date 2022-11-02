class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank=set(bank)
        
        q=deque([[start,0]])
        visited={start}
        
        while q:
            now,d=q.popleft()
            if now==end:
                return d
            for next in 'ACTG':
                for i in range(8):
                    tmp = now[:i]+next+now[i+1:]
                    if tmp in bank and tmp not in visited:
                        q.append([tmp,d+1])
                        visited.add(tmp)
        return -1