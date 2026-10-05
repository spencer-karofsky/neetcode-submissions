class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init_color = image[sr][sc]

        def dfs(r, c):
            # check out of bounds
            if r < 0 or c < 0 or r > len(image) - 1 or c > len(image[0]) - 1:
                return
            
            # check if init_color and not already colored
            if image[r][c] != init_color or image[r][c] == color:
                return

            # color pixel
            image[r][c] = color

            # adjacent cell calls
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return
        

        dfs(sr, sc)

        return image