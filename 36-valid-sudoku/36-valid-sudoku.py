class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkrow(num, r):
            cnt=0
            for n in board[r]:
                if n==num:
                    cnt+=1
                if cnt==2:
                    return False
            return True
        
        def checkcol(num, c):
            cnt=0
            for j in range(9):
                n=board[j][c]
                if n==num:
                    cnt+=1
                if cnt==2:
                    return False
            return True
        
        def checkbox(num,r,c):
            r-=(r%3)
            c-=(c%3)
            cnt=0
            for rr in range(r,r+3):
                for cc in range(c,c+3):
                    n=board[rr][cc]
                    if n==num:
                        cnt+=1
                    if cnt==2:
                        return False
            return True
        
        for i in range(9):
            for j in range(9):
                if board[i][j].isnumeric():
                    if not (checkrow(board[i][j],i) and checkcol(board[i][j],j) and checkbox((board[i][j]),i,j)):
                        return False
        
        return True