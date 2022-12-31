class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def solve(i, j, c):
            if(not(0<=i<m and 0<=j<n) or grid[i][j] == -1):
                return 0
            if(grid[i][j] == 2):
                return len(vis) == m*n-1-c
            vis.add((i, j))
            temp = 0
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if((i+x, j+y) not in vis):
                    temp += solve(i+x, j+y, c)
            vis.remove((i, j))
            return temp

        vis = set()
        c = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    si, sj = i, j
                if(grid[i][j] == -1):
                    c += 1
        return solve(si, sj, c)