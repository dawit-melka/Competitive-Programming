class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows, cols = len(grid), len(grid[0])
        startR, startC = 0, 0
        countKeys = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def isInbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] not in['.','#','@'] and grid[r][c].islower():
                    countKeys += 1
                elif grid[r][c] == '@':
                    startR, startC = r, c
        
        queue = deque([[startR, startC, set()]])
        visited = set([(startR, startC, tuple())])
        ans = 0
        while queue:
            for _ in range(len(queue)):
                r, c, keys = queue.popleft()
                if len(keys) == countKeys:
                    return ans
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if isInbound(nr, nc) and (nr, nc, tuple(sorted(keys))) not in visited:
                        if grid[nr][nc] == '.' or grid[nr][nc] == '@':
                            queue.append([nr, nc, keys.copy()])
                            visited.add((nr, nc, tuple(sorted(keys))))

                        elif grid[nr][nc] == '#':
                            continue
                        elif grid[nr][nc].islower():
                            newKeys = keys.copy()
                            newKeys.add(grid[nr][nc])
                            queue.append([nr, nc, newKeys])
                            visited.add((nr, nc, tuple(sorted(newKeys))))
                        elif grid[nr][nc].lower() in keys:
                                queue.append([nr, nc, keys.copy()])
                                visited.add((nr, nc, tuple(sorted(keys))))

            ans += 1

        return -1
