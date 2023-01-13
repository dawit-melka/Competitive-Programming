class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        maxLocal = [[0]*(COLS-2) for _ in range(ROWS-2)]

        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                maxVal = max(grid[r-1][c-1], grid[r-1][c], grid[r-1][c+1],
                            grid[r][c-1], grid[r][c], grid[r][c+1],
                            grid[r+1][c-1], grid[r+1][c], grid[r+1][c+1])
                            
                maxLocal[r-1][c-1] = maxVal
        
        return maxLocal
