class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dr=[1,-1,0,0]
        dc=[0,0,1,-1]
        R=len(board)
        C=len(board[0])
        N=len(word)
        K=False
        
        def dfs(r,c,n,visited):
            nonlocal K
            if n==0:
                visited[r][c]=1
            if n==N-1:
                K=True
                return

            for i in range(4):
                rr=r+dr[i]
                cc=c+dc[i]
                if 0<=rr<R and 0<=cc<C and board[rr][cc]==word[n+1] and not visited[rr][cc]:
                    visited[rr][cc]=1
                    dfs(rr,cc,n+1,visited)
                    visited[rr][cc]=0
            
            return False
        
        
        for i in range(R):
            for j in range(C):
                if board[i][j]==word[0]:
                    dfs(i,j,0,[[0]*C for _ in range(R)])
                    if K:return True
        
        return False