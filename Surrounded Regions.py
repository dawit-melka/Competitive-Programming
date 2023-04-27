class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def inBound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def dfs(row, col):
            if not inBound(row, col) or board[row][col] in ["X", "V"]:
                return

            board[row][col] = "V"
            for dx, dy in directions:
                dfs(row + dx, col + dy)


        for row in range(len(board)):
            dfs(row, 0)
            dfs(row, len(board[0])-1)
        
        for col in range(len(board[0])):
            dfs(0, col)
            dfs(len(board)-1, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "V":
                    board[row][col] = "O"
