class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        m, n = len(grid), len(grid[0])

        from collections import deque

        queue = deque()
        visited = set()

        queue.append((0, 0, 1))
        visited.add((0, 0))

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        shortest = 0
        while queue:
            r, c, dist = queue.popleft()
            if r == m - 1 and c == n - 1:
                return dist
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nc < 0 or nr == m or nc == n or grid[nr][nc] == 1 or (nr, nc) in visited:
                    continue
                queue.append((nr, nc, dist + 1))
                visited.add((nr, nc))
        return -1
                


