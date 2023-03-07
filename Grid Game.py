class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        if n == 1:
            return 0
        for i in range(n-2, -1, -1):
            grid[0][i] += grid[0][i+1]
        for i in range(1, n):
            grid[1][i] += grid[1][i-1]

        for i in range(n):
            if  i + 1 < n and grid[1][i] >= grid[0][i+1]:
                if i-1 >= 0:
                    return max(grid[0][i+1], grid[1][i-1])
                else:
                    return grid[0][i+1]
            elif i+1 == n:
                return grid[1][i-1]
