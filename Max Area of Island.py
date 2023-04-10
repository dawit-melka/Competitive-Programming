class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            if (not inBound(row, col) or
                (row, col) in visited or
                not grid[row][col]):
                return 0
            visited.add((row, col))
            count = 0
            for dx, dy in directions:
                count += dfs(row + dx, col + dy)

            return 1 + count
        
        result = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] and (row, col) not in visited:
                    result = max(result, dfs(row, col))


        return result
