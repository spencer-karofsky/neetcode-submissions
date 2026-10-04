class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()

        def dfs(r, c, init_color):
            if r < 0 or c < 0 or r > len(image) - 1 or c > len(image[0]) - 1:
                return
            if (r, c) in visited:
                return
            if image[r][c] != init_color:
                return
            visited.add((r, c))
            image[r][c] = color
            dfs(r + 1, c, init_color)
            dfs(r - 1, c, init_color)
            dfs(r, c + 1, init_color)
            dfs(r, c - 1, init_color)

        init_color = image[sr][sc]
        dfs(sr, sc, init_color)
        
        return image
