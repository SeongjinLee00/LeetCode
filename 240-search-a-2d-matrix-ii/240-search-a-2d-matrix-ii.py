class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        i = n-1
        j = 0
        while i>=0 and j <m:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i-=1
            else:
                j+=1
        return False