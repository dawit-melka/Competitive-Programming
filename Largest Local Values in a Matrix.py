class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        maxLocal = [[0]*(COLS-2) for _ in range(ROWS-2)]

        for r in range(ROWS-2):
            for c in range(COLS-2):
                maxVal = max(grid[r][c], grid[r][c+1], grid[r][c+2],
                            grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                            grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2])
                maxLocal[r][c] = maxVal
        
        return maxLocal
