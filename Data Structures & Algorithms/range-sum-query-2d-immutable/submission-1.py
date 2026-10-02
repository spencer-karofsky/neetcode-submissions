class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # Solution: O(R*C)~O(n^2) time and space
        R, C = len(matrix), len(matrix[0])
        # mat_sum[r][c] = sum of all elements in the region
        # between matrix[0][0] and matrix[r - 1][c]
        self.mat_sum = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            prefix = 0
            for c in range(C):
                prefix += matrix[r][c]
                above = self.mat_sum[r][c + 1]
                self.mat_sum[r + 1][c + 1] = above + prefix       

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Solution: O(1) time and space lookup
        # sum of all elements in the region
        # is prefix sum's bottom right - above area - left area + top left
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return (
            self.mat_sum[row2][col2] - # bottom right
            self.mat_sum[row1 - 1][col2] - # above
            self.mat_sum[row2][col1 - 1] + # left
            self.mat_sum[row1 - 1][col1 - 1] # top left
        )

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)