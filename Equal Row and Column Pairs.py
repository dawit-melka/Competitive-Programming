class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count_rows = {}
        res = 0
        n = len(grid)

        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in count_rows:
                count_rows[row_tuple] += 1
            else:
                count_rows[row_tuple] = 1

        for c in range(n):
            col_vals = []
            for r in range(n):
                col_vals.append(grid[r][c])
            
            col_tuple = tuple(col_vals)
            if col_tuple in count_rows:
                res += count_rows[col_tuple]

        return res
