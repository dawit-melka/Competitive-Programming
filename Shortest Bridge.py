class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            if not inBound(row, col) or grid[row][col] != 1:
                return
            
            grid[row][col] = 2
            for dx, dy in directions:
                dfs(row+dx, col+dy)
        found = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row, col)
                    found = True
                    break
            if found:
                break
        
        queue = deque()
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    queue.append((row, col, -1))
                    visited.add((row, col))
        
        while queue:
            row, col, dis = queue.popleft()
            if grid[row][col] == 2:
                return dis
            
            for dx, dy in directions:
                r, c = row+dx, col+dy
                if inBound(r, c) and (r, c) not in visited and grid[r][c] != 1:
                    visited.add((r, c))
                    queue.append((r, c, dis+1))
        
        return 0
