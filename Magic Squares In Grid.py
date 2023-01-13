class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(2, ROWS):
            for c in range(2, COLS):
                one_to_nine = [0]*10
                if 1 <= grid[r-2][c-2] <= 9:
                    if one_to_nine[grid[r-2][c-2]] > 0:
                        continue
                    one_to_nine[grid[r-2][c-2]] = 1
                else: continue

                if 1 <= grid[r-2][c-1] <= 9:
                    if one_to_nine[grid[r-2][c-1]] > 0:
                        continue
                    one_to_nine[grid[r-2][c-1]] = 1
                else: continue

                if 1 <= grid[r-2][c] <= 9:
                    if one_to_nine[grid[r-2][c]] > 0:
                        continue
                    one_to_nine[grid[r-2][c]] = 1
                else: continue

                if 1 <= grid[r-1][c-2] <= 9:
                    if one_to_nine[grid[r-1][c-2]] > 0:
                        continue
                    one_to_nine[grid[r-1][c-2]] = 1
                else: continue

                if 1 <= grid[r-1][c-1] <= 9:
                    if one_to_nine[grid[r-1][c-1]] > 0:
                        continue
                    one_to_nine[grid[r-1][c-1]] = 1
                else: continue

                if 1 <= grid[r-1][c] <= 9:
                    if one_to_nine[grid[r-1][c]] > 0:
                        continue
                    one_to_nine[grid[r-1][c]] = 1
                else: continue

                if 1 <= grid[r][c-2] <= 9:
                    if one_to_nine[grid[r][c-2]] > 0:
                        continue
                    one_to_nine[grid[r][c-2]] = 1
                else: continue

                if 1 <= grid[r][c-1] <= 9:
                    if one_to_nine[grid[r][c-1]] > 0:
                        continue
                    one_to_nine[grid[r][c-1]] = 1
                else: continue

                if 1 <= grid[r][c] <= 9:
                    if one_to_nine[grid[r][c]] > 0:
                        continue
                    one_to_nine[grid[r][c]] = 1
                else: continue

                sum_r0 = grid[r-2][c-2] + grid[r-2][c-1] + grid[r-2][c]
                sum_r1 = grid[r-1][c-2] + grid[r-1][c-1] + grid[r-1][c]
                sum_r2 = grid[r][c-2] + grid[r][c-1] + grid[r][c]
                sum_c0 = grid[r-2][c-2] + grid[r-1][c-2] + grid[r][c-2]
                sum_c1 = grid[r-2][c-1] + grid[r-1][c-1] + grid[r][c-1]
                sum_c2 = grid[r-2][c] + grid[r-1][c] + grid[r][c]
                diag1 = grid[r-2][c-2] + grid[r-1][c-1] + grid[r][c]
                diag2 = grid[r-2][c] + grid[r-1][c-1] + grid[r][c-2]
                if sum_r0 == sum_r1 == sum_r2 == sum_c0 == sum_c1 == sum_c2 == diag1 == diag2:
                    count += 1

        return count
