class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        n = len(grid)
        queue = deque([(0, 0, 1)])
        directions = [(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1),(0,1),(0,-1)]

        def inBound(row, col):
            return 0 <= row < n and 0 <= col < n

        while queue:
            row, col, dis = queue.popleft()
            if row == n-1 and col == n-1:
                return dis

            for dx, dy in directions:
                if inBound(row+dx, col+dy) and grid[row+dx][col+dy] == 0:
                    grid[row+dx][col+dy] = 1
                    queue.append((row+dx, col+dy, dis+1)) 

        return -1
