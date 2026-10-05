class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        queue = deque()

        fresh = 0
        rotten = set()

        m, n = len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0)) # r, c, time
                    rotten.add((r, c))

        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_time = 0
        while queue:
            r, c, time = queue.popleft()
            max_time = max(max_time, time)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not 0 <= nr <= m - 1 or not 0 <= nc <= n - 1:
                    continue
                if (nr, nc) not in rotten and grid[nr][nc] == 1:
                    fresh -= 1
                    grid[nr][nc] = 2
                    queue.append((nr, nc, time + 1))
                    rotten.add((nr, nc))
        if fresh == 0:
            return max_time
        return -1
