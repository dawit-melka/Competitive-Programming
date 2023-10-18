class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        rep = {}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inBound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def explore(row, col, par):
            if not inBound(row, col) or grid[row][col] == 0 or visited[row][col] != 0:
                return 0
            currCount = 0
            visited[row][col] = par
            for dx, dy in directions:
                currCount += explore(row+dx, col+dy, par)
            
            return currCount + 1
        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                currArea = explore(r, c, (r, c))
                if currArea > 0:
                    rep[(r, c)] = currArea
                    result = max(result, rep[(r, c)])
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    up = None if (r-1 < 0 or grid[r-1][c] == 0) else visited[r-1][c]
                    down = None if (r+1 == len(grid) or grid[r+1][c] == 0) else visited[r+1][c]
                    left = None if (c-1 < 0 or grid[r][c-1] == 0) else visited[r][c-1]
                    right = None if (c+1 == len(grid[0]) or grid[r][c+1] == 0) else visited[r][c+1]
                    currArea = 1
                    for curr in set([up, down, left, right]):
                        if curr == None:
                            continue
                        currArea += rep[curr]
                    result = max(result, currArea)


        return result
