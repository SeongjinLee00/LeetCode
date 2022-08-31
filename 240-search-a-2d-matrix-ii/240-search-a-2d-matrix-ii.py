class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        
        r=n-1
        c=0
        
        while True:
            if matrix[r][c]>target:
                r-=1
            elif matrix[r][c]<target:
                c+=1
            else:
                return True
            if r==-1 or c==m:
                return False