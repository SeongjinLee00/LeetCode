class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N=len(dominoes)
        answer=['.']*N
        time=[0]*N

        q=deque()
        for i in range(N):
            if not dominoes[i]=='.':
                q.append([i,dominoes[i],0])
                answer[i]=dominoes[i]

        while q:
            i,d,t=q.popleft()
            if d=='R' and i+1<N:
                if answer[i+1]=='.':
                    q.append([i+1,'R',t+1])
                    answer[i+1]='R'
                    time[i+1]=t+1
                elif answer[i+1]=='L' and time[i+1]==t+1:
                    answer[i+1]='.'

            elif d=='L' and i-1>=0:
                if answer[i-1]=='.':
                    q.append([i-1,'L',t+1])
                    answer[i-1]='L'
                    time[i-1]=t+1
                elif answer[i-1]=='R' and time[i-1]==t+1:
                    answer[i-1]='.'

        return "".join(answer)