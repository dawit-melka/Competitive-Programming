class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"

        def inBound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        while queue:
            row, col, dis = queue.popleft()
            
            if dis and (row == 0 or row == rows-1 or col == 0 or col == cols-1):
                return dis
            
            for dx, dy in directions:
                curr_row, curr_col = row + dx, col + dy
                if inBound(curr_row, curr_col) and maze[curr_row][curr_col] == ".":
                    queue.append((curr_row, curr_col, dis+1))
                    maze[curr_row][curr_col] = "+"

        return -1
