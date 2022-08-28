class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        R=len(mat)
        C=len(mat[0])

        def bubblesort(r,c):
            originr=r
            originc=c
            for _ in range(max(R,C)):
                r=originr
                c=originc
                while True:
                    if r==R-1 or c==C-1:
                        break
                    if mat[r+1][c+1]<mat[r][c]:
                        mat[r][c], mat[r+1][c+1] = mat[r+1][c+1], mat[r][c]
                    r+=1
                    c+=1

        for row in range(R-1,-1,-1):
            bubblesort(row,0)
        for column in range(1,C):
            bubblesort(0,column)
        return mat