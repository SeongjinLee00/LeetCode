class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        r=len(board)
        c=len(board[0])
        
        if r==1 and c==1:
            board[0][0]=0
        if r==1 and c==2:
            board[0][0]=0
            board[0][1]=0
        if r==2 and c==1:
            board[0][0]=0
            board[1][0]=0
            
        d=defaultdict(int)
        
        dr=[1,-1,0,0,1,1,-1,-1]
        dc=[0,0,1,-1,1,-1,1,-1]
        for i in range(r):
            for j in range(c):
                for k in range(8):
                    rr=i+dr[k]
                    cc=j+dc[k]
                    if 0<=rr<r and 0<=cc<c:
                        d[(rr,cc)]+=board[i][j]
        
        die=set()
        live=set()

        for k, v in d.items():
            r=k[0]
            c=k[1]
            
            if board[r][c] and not (v==2 or v==3):
                die.add((r,c))
            if not board[r][c] and v==3:
                live.add((r,c))
        
        for r,c in die:
            board[r][c]=0
        for r,c in live:
            board[r][c]=1