class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        directions = [(1, 0), (-1,0), (0,1), (0,-1)]
        isSubIsland = True
        count = 0

        def inBound(row, col):
            return 0 <= row < len(grid2) and 0 <= col < len(grid2[0])

        def dfs(row, col):
            if not inBound(row, col) or grid2[row][col] == 0 or (row, col) in visited:
                return
            if grid1[row][col] == 0:
                nonlocal isSubIsland
                isSubIsland = False
            
            visited.add((row,col))
            for dx, dy in directions:
                dfs(row+dx, col+dy)

        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] and (row,col) not in visited:
                    isSubIsland = True
                    dfs(row, col)
                    if isSubIsland:
                        count += 1

        return count
