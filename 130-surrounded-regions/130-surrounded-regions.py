class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R=len(board)
        C=len(board[0])
        
        visited=[[0]*C for _ in range(R)]
        
        dr=[1,-1,0,0]
        dc=[0,0,1,-1]
        
        def bfs(r,c):
            q=deque([[r,c]])
            visited[r][c]=1
            board[r][c]='N'
            
            while q:
                r,c=q.popleft()
                for k in range(4):
                    rr=r+dr[k]
                    cc=c+dc[k]
                    if 0<=rr<R and 0<=cc<C and board[rr][cc]=='O' and not visited[rr][cc]:
                        board[rr][cc]='N'
                        q.append([rr,cc])
                        visited[rr][cc]=1
        
        for j in range(C):
            i=0
            ii=R-1
            if board[i][j]=='O':
                bfs(i,j)
            if board[ii][j]=='O':
                bfs(ii,j)
                
        for i in range(R):
            j=0
            jj=C-1
            if board[i][j]=='O':
                bfs(i,j)
            if board[i][jj]=='O':
                bfs(i,jj)
        
        for i in range(R):
            for j in range(C):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='N':
                    board[i][j]='O'