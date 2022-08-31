class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        left=0
        right=n*m
        
        while True:
            mid=(left+right)//2
            
            i=mid//m
            j=mid%m
            
            if matrix[i][j]>target:
                right=mid
            else:
                left=mid
                
            if right-left<=1:
                return bool(matrix[left//m][left%m]==target)