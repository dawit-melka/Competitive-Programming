class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        ones_rows_count = [0]*rows
        ones_cols_count = [0]*cols

        for r in range(rows):
            for c in range(cols):
                ones_rows_count[r] += grid[r][c]
                ones_cols_count[c] += grid[r][c]
        
        res = []
        for _ in range(rows):
            res.append([0]*cols)

        for r in range(rows):
            for c in range(cols):
                res[r][c] = 2*ones_rows_count[r] + 2*ones_cols_count[c] - rows - cols
        
        return res
