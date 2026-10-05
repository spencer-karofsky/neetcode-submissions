class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()

        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r > m - 1 or c > n - 1 or grid[r][c] == 0 or (r, c) in visit:
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
        
        area = 0
        for r in range(m):
            for c in range(n):
                area = max(area, dfs(r, c))
        return area