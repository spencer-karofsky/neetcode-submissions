class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if not 0 <= r <= m - 1 or not 0 <= c <= n - 1:
                return
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1),
            dfs(r, c - 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        return islands
            
             
